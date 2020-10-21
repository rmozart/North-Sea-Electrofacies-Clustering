import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_well_logs(df, name):

    fig = plt.figure()

    fig.set_size_inches(15, 12)

    well_name = name

    ax1 = plt.subplot(1,5,1)
    ax1.plot(df[df['WELL_NAME'] == well_name].GR, df[df['WELL_NAME'] == well_name].DEPTH, 'g', linewidth = 1, label='GR')
    ax1.invert_yaxis()
    ax1.tick_params(which='both', width=1)
    ax1.grid()
    ax1.set_ylabel('Depth (m)', fontsize=16)
    ax1.set_xlabel('API', fontsize=16)
    ax1.set_title('GR', fontsize=16)
    ax1.set_xlim(df[df['WELL_NAME'] == well_name].GR.min(),df[df['WELL_NAME'] == well_name].GR.max())

    #_____________________________________________________#

    ax2 = plt.subplot(1,5,2)
    ax2.plot(df[df['WELL_NAME'] == well_name].RHOB, df[df['WELL_NAME'] == well_name].DEPTH, 'r', linewidth = 1, label='RHOB')
    ax2.invert_yaxis()
    ax2.grid()
    ax2.set_yticklabels([])
    ax2.set_xlabel('g/cc', fontsize=16)
    ax2.set_title('RHOB', fontsize=16)
    ax2.set_xlim(df[df['WELL_NAME'] == well_name].RHOB.min(),df[df['WELL_NAME'] == well_name].RHOB.max())

    #_____________________________________________________#

    ax3 = plt.subplot(1,5,3)
    ax3.plot(df[df['WELL_NAME'] == well_name].NPHI, df[df['WELL_NAME'] == well_name].DEPTH, 'b', linewidth = 1, label='NPHI')
    ax3.invert_yaxis()
    ax3.grid()
    ax3.set_yticklabels([])
    ax3.set_xlabel('m3/m3', fontsize=16)
    ax3.set_title('NPHI', fontsize=16)
    ax3.set_xlim(df[df['WELL_NAME'] == well_name].NPHI.min(),df[df['WELL_NAME'] == well_name].NPHI.max())

    #_____________________________________________________#

    ax4 = plt.subplot(1,5,4)
    ax4.plot(df[df['WELL_NAME'] == well_name].DTC, df[df['WELL_NAME'] == well_name].DEPTH, 'k', linewidth = 1, label='DTC')
    ax4.invert_yaxis()
    ax4.grid()
    ax4.set_yticklabels([])
    ax4.set_xlabel('us/ft', fontsize=16)
    ax4.set_title('DTC', fontsize=16)
    ax4.set_xlim(df[df['WELL_NAME'] == well_name].DTC.min(),df[df['WELL_NAME'] == well_name].DTC.max())
    
    #_____________________________________________________#

    ax5 = plt.subplot(1,5,5)
    ax5.semilogx(df[df['WELL_NAME'] == well_name].RDEP, df[df['WELL_NAME'] == well_name].DEPTH, 'm', linewidth = 1, label='RDEP')
    ax5.invert_yaxis()
    ax5.grid()
    ax5.set_xscale('log')
    ax5.set_yticklabels([])
    ax5.set_xlabel('ohm.m', fontsize=16)
    ax5.set_title('RDEP', fontsize=16)
    ax5.set_xlim(df[df['WELL_NAME'] == well_name].RDEP.min(),df[df['WELL_NAME'] == well_name].RDEP.max())

    return plt.show()