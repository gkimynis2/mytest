import os
import pandas as pd
import time

#read and write functions
def readwrite(input_file,output_file):
        data = pd.read_csv(input_file, sep=',', header=None)
        data = pd.read_csv(input_file, sep=',', header=None)
        data.to_csv(output_file, sep=',', columns={9, 10, 14}, header=None, index=False)

#timing function
def getRunTimes( fun ,input_file,output_file):
        begin_time=int(round(time.time() * 1000))
        fun(input_file,output_file)
        end_time=int(round(time.time() * 1000))
        print('Data processing completed')
        print("Data processing total time：",(end_time-begin_time),"ms")
#transfer

input_file="C:/Users/XXX/Desktop/event_masked.csv"
output_file="C:/Users/XXX/Desktop/new_event_masked.csv"

if  os.access(output_file, os.F_OK):
        print('The file already exists, and the write is generated after the delete file operation is performed ')
        os.remove(output_file)
        readwrite(input_file,output_file)
        getRunTimes(readwrite,input_file,output_file)
else:
        readwrite(input_file, output_file)
        getRunTimes(readwrite, input_file, output_file)

