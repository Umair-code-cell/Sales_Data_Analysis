# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import csv

#import the input file fact.csv
ifile='D:file_pro\fact.csv'

#create the three output files for each fact
ogpu='D:file_pro\factGPU.csv'
ocpu='D:file_pro\factCPU.csv'
oram='D:file_pro\factRAM.csv'

#open the input file, set the reader for read each line and the see the attributes value 
fact=open(ifile)
lines = csv.reader(fact, delimiter = ',')
attrs = fact.readline().strip().split(',') 

#open the output file for the GPU and write the first row with the value of the column
outgpu = open(ogpu,"w")
outgpu.write(attrs[0] +","+ attrs[1] +","+ attrs[4] +","+ attrs[5] +","+ attrs[6] +","+ attrs[7] +","+ attrs[8] +"\n")

#open the output file for the CPU and write the first roe with the value of the column
outcpu = open(ocpu,"w")
outcpu.write(attrs[0] +","+ attrs[2] +","+ attrs[4] +","+ attrs[5] +","+ attrs[6] +","+ attrs[7] +","+ attrs[8] +"\n")

#open the output file for the RAM and write the first roe with the value of the column
outram = open(oram,"w")
outram.write(attrs[0] +","+ attrs[3] +","+ attrs[4] +","+ attrs[5] +","+ attrs[6] +","+ attrs[7] +","+ attrs[8] +"\n")

#variables count for each case just for a check
countG=0
countC=0
countR=0

#start the loop for splitting the input file
for row in lines:
        #GPU case
        if row[1] != '':
            outgpu.write(row[0] +","+ row[1] +","+ row[4] +","+ row[5] +","+ row[6] +","+ row[7] +","+ row[8] +"\n")
            countG=countG+1
        #CPU case
        elif row[2] != '':
            outcpu.write(row[0] +","+ row[2] +","+ row[4] +","+ row[5] +","+ row[6] +","+ row[7] +","+ row[8] +"\n")
            countC=countC+1
        #RAM case
        elif row[3] != '':
            outram.write(row[0] +","+ row[3] +","+ row[4] +","+ row[5] +","+ row[6] +","+ row[7] +","+ row[8] +"\n")
            countR=countR+1
            
#Done allert and count check
print("copied " +str(countG)+ " rows in factGPU.csv")
print("done with GPU \n")
print("copied " +str(countC)+ " rows in factCPU.csv")
print("done with CPU \n")
print("copied " +str(countR)+ " rows in factRAM.csv")
print("done with RAM \n")

#Close all the output files
outram.close()
outcpu.close()
outgpu.close()


