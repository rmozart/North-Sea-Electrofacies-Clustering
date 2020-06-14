import pandas as pd
import numpy as np
import os
from os import path
import lasio
from tqdm import tqdm
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

    for i in tqdm(((os.listdir(path_to_folder))), desc="Reading all las files from folder"):
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
        for file in tqdm(files, desc='Reading las files from' + ' ' + subdir):
            if os.path.splitext(file)[1] == '.las':
                main_name[os.path.splitext(file)[0]] = lasio.read(os.path.join(subdir, file))
    
    return main_name