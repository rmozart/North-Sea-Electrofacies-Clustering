import pandas as pd
import numpy as np
import os
from os import path
import lasio
from tqdm import tqdm_notebook
import logging
logging.getLogger("lasio").setLevel(logging.ERROR)


def read_las_directory(path_to_folder):
    """Reads all las files on the given folder.

    Args:
      path_to_folder: entire path to the las files storage folder.
    Returns:
      main_name: dictionary of las files IDs as keys and lasio type for each file.
    """

    main_name = {}

    for i in tqdm_notebook(((os.listdir(path_to_folder))), desc="Reading all las files from folder"):
        main_name[os.path.splitext(i)[0]] = lasio.read(os.path.join(path_to_folder, i))

    return main_name

def search_and_read_las_directories(path_to_main_folder):
    """Reads and search all las files on the given folder and its subdirectories.

    WARNING: This function does not ensures that the las files will have any correlation with each other,
    since it iterates through the entire given folder and it subsequent sub-folders.

    Args:
      path_to_main_folder: entire path to the main folder where the las files are stored in several different folders.
    Returns:
      main_name: dictionary of las files IDs as keys and lasio type for each file.
    """

    main_name = {}

    for subdir, dirs, files in os.walk(path_to_main_folder):
        for file in tqdm_notebook(files, desc='Reading las files from' + ' ' + subdir):
            if os.path.splitext(file)[1] == '.las':
                main_name[os.path.splitext(file)[0]] = lasio.read(os.path.join(subdir, file))
    
    return main_name

def unit_check(las_dict):
    """Checks possible unmatchings of unit of measurement for each log curve within the entire given las dictionary.
    Args:
      las_dict: dictionary of several las files to be checked.
    Returns:
      flag: list of las files ids and its correlated log curves with the given mismatched unit of measurements.
    """

    flag = [] # list of flags in which logs on all las files have a different unit of measurement

    for id in tqdm_notebook(list(las_dict.keys()), desc='Checking unmatching unit of measurements'): # iterating over all las files

        tmp = list(las_dict.keys()) # initiating list of key to remove correct las file on further loop

        tmp.remove(id) # removing current las file from list of wells to compare with it

        for log in las_dict[id].curves.keys(): # iterating over all available logs given the current las file

            for comp in tmp: # iterating over all las files excepet the given one

                if log in las_dict[comp].curves.keys(): # checking if comparative well has given log from las file reference

                    if las_dict[id].curves[log].unit != las_dict[comp].curves[log].unit: # check if the unit of measurement are not the same given that the log exists on the comparative well file

                        flag.append([(id, comp), (log), (las_dict[id].curves[log].unit, las_dict[comp].curves[log].unit)]) # attach list of tuples to the flag list indicating both wells ids the "misleading" and both units

    print('\n')
    print('It was found a total of' + ' ' + str(len(flag)) + ' ' + 'unmatching unit of measurement in the dataset. Please, check the flag output for proper adjustments')

    return flag

def log_frame(data, logs, mode='df'):
    """Create a dataframe per each given log data informed. 
    Args:
      data: dictionary of several las files to be checked or a dictionary of several dataframes, whereas the columns are the logs mnemonics.
      mode: entry of data mode: 'df' for Pandas Dataframe type or 'las' for lasio objects
      logs: list of the logs mneumonics to be selected
    Returns:
      logs_dict: a dictionary with a dataframe per each given log mnemonic. The keys are equal to each element of the logs mnemonics list
    """    

    if mode == 'las': # still in progress

      return
    
    elif mode == 'df': # if the mode is df

      logs_dict = {} # create empty dictionary

      for log_curve in tqdm_notebook(logs, desc='Filling in Dictionary'): # iterate over all requested logs

        tmp_list_well_id = [] # for each log create an empty list to store all wells ids to name the columns

        logs_dict[log_curve] = pd.DataFrame() # for each log create an empty dateframe and the respective key for the dictionary

        for well_id in list(data.keys()): # iterate over all the las files

          if log_curve in data[well_id].columns: # if the given log curve exists in the las file

            tmp_list_well_id.append(well_id) # we store its id

            logs_dict[log_curve] = pd.concat([logs_dict[log_curve], data[well_id][log_curve]], axis=1) # concatenate the curve as a column on the log dataframe

            logs_dict[log_curve].columns = tmp_list_well_id # and replace the columns names by the wells ids

      return logs_dict

    else:

      raise TypeError('Unrecognized mode type. Possibles modes are \'df\' and \'las\'')

      return


