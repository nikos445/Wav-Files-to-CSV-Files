"""
@author: Nikolaos Astyrakakis

@based on: Lukious 
https://github.com/Lukious/wav-to-csv/blob/master/wav2csv.py
"""

import sys, os, os.path
from scipy.io import wavfile
import pandas as pd

folder_files = os.listdir("input")
print(folder_files)
 
for file in folder_files:
    samrate, data = wavfile.read(str('./input/' + file)) 

    wavData = pd.DataFrame(data)

    if len(wavData.columns) == 2:
        print('Stereo .wav file\n')
        wavData.columns = ['R', 'L']
        stereo_R = pd.DataFrame(wavData['R'])
        stereo_L = pd.DataFrame(wavData['L']) 
        stereo_R.to_csv(str('./output/' +file[:-4] + "stereo_R.csv"), mode='w')
        stereo_L.to_csv(str('./output/' +file[:-4] + "stereo_L.csv"), mode='w') 
        print('Save is done ' + str('./output/' +file[:-4]) + 'stereo_R.csv , '
                              + str('./output/' +file[:-4]) + 'stereo_L.csv')

    elif len(wavData.columns) == 1:
        print('Mono .wav file\n')
        wavData.columns = ['M'] 
        wavData.to_csv(str('./output/' +file[:-4] + "mono.csv"), mode='w') 
        print('Save is done ' + str('./output/' +file[:-4]) + 'mono.csv')

    else:
        print('Multi channel .wav file\n')
        print('number of channel : ' + len(wavData.columns) + '\n')
        wavData.to_csv(str('./output/' +file[:-4] + " multi_channel.csv"), mode='w') 
        print('Save is done ' + str('./output/' +file[:-4]) + ' multi_channel.csv')
