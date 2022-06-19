# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 11:59:20 2020

@author: Riccardo
"""

import pyodbc
import csv
import datetime

#Set up the connection
server = 'tcp:apa.di.unipi.it' 
database = 'Group21HWMart' 
username = 'group21' 
password = 'z0sqm' 
connectionString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password

#Geography CASE
#-----------------------------

#open connection
cnxn = pyodbc.connect(connectionString)
cursor = cnxn.cursor()

#import file and prepare it
ifile='D:file_pro\geography.csv'
geo=open(ifile)
lines = csv.reader(geo, delimiter = ',')

#Prepare SQL query
sql ="INSERT INTO Geography(geo_code,continent,country,region,currency) VALUES(?,?,?,?,?)"

print("Start the loading in geography")
count=0

#Start the loading
for row in lines:
    rows= cursor.execute(sql, (int(row[0]), row[1], row[2], row[3], row[4]))
    count=count+1
    if count % 10 == 0:
        print("Loaded " +str(count)+ " rows")

#Close connection and file
cnxn.commit()
geo.close()

print("Done geography")

print("Loaded " +str(count)+ " rows in geography \n")



#Vendor CASE
#-----------------------------

#same procedure, no comment inserted
cnxn = pyodbc.connect(connectionString)

cursor = cnxn.cursor()

ifile='D:file_pro/vendor.csv'
ven=open(ifile)
lines = csv.reader(ven, delimiter = ',')
attrs = ven.readline().strip().split(',')


sql ="INSERT INTO Vendor(vendor_code,name) VALUES(?,?)"

print("Start the loading in vendor")
count=0
for row in lines:
    rows= cursor.execute(sql, (int(row[0]), row[1]))
    count=count+1
    if count % 10 ==0:
        print("Loaded " +str(count)+ " rows")
    
    
cnxn.commit()
ven.close()

print("Done vendor")

print("Loaded " +str(count)+ " rows in vendor \n")

#Cpu_product CASE
#-----------------------------

#same procedure, no comment inserted
cnxn = pyodbc.connect(connectionString)

cursor = cnxn.cursor()

ifile='D:file_pro\cpu.csv'
cpu=open(ifile)
lines = csv.reader(cpu, delimiter = ',')
attrs = cpu.readline().strip().split(',')

sql ="INSERT INTO Cpu_product(cpu_code,brand,series,name,n_cores,socket) VALUES(?,?,?,?,?,?)"

print("Start the loading in Cpu_product")
count=0
for row in lines:
    rows= cursor.execute(sql, (int(row[0]), row[1], row[2], row[3], int(row[4]), row[5]))
    count=count+1
    if count % 10 ==0:
        print("Loaded " +str(count)+ " rows")
    
cnxn.commit()
cpu.close()

print("done Cpu_product")
print("Loaded " +str(count)+ " rows in Cpu_product \n")


#Gpu_product CASE
#-----------------------------

#same procedure, no comment inserted

cnxn = pyodbc.connect(connectionString)

cursor = cnxn.cursor()

ifile='D:file_pro/gpu.csv'
gpu=open(ifile)
lines = csv.reader(gpu, delimiter = ',')
attrs = gpu.readline().strip().split(',')

sql ="INSERT INTO Gpu_product(gpu_code,processor,processor_manufacturer,brand,memory,memory_type) VALUES(?,?,?,?,?,?)"

print("Start the loading in Gpu_product")
count=0
for row in lines:
    rows= cursor.execute(sql, (int(row[0]), row[1], row[2], row[3], float(row[4]), row[5]))
    count=count+1
    if count % 10 ==0:
        print("Loaded " +str(count)+ " rows")
    
cnxn.commit()
gpu.close()

print("done Gpu_product")
print("Loaded " +str(count)+ " rows in Gpu_product \n")


#Ram_product CASE
#-----------------------------

#same procedure, no comment inserted

cnxn = pyodbc.connect(connectionString)

cursor = cnxn.cursor()

ifile='D:file_pro/ram.csv'
ram=open(ifile)
lines = csv.reader(ram, delimiter = ',')
attrs = ram.readline().strip().split(',')

sql ="INSERT INTO Ram_product(ram_code,brand,name,memory,memory_type,clock) VALUES(?,?,?,?,?,?)"

print("Start the loading in Ram_product")
count=0
for row in lines:
    rows= cursor.execute(sql, (int(row[0]), row[1], row[2], float(row[3]), row[4], int(row[5])))
    count=count+1
    if count % 10 ==0:
        print("Loaded " +str(count)+ " rows")
    
cnxn.commit()
ram.close()

print("done Ram_product")
print("Loaded " +str(count)+ " rows in Ram_product \n")


#Time CASE
#-----------------------------

#same procedure except for the new attributes

cnxn = pyodbc.connect(connectionString)

cursor = cnxn.cursor()

ifile='D:file_pro/time.csv'
time=open(ifile)
lines = csv.reader(time, delimiter = ',')
attrs = time.readline().strip().split(',')

sql ="INSERT INTO time(time_id,year,month,day,week,quarter,day_of_week) VALUES(?,?,?,?,?,?,?)"

print("Start the loading in time")
count=0

for row in lines:
    
    #If for checking which quarter is
    if int(row[2])in range (1,4):
        quarter="Q1"
    elif int(row[2])in range (4,7):
        quarter="Q2"
    elif int(row[2])in range (7,10):
        quarter="Q3"
    else:
        quarter="Q4"

    #Get the name of the day thanks to the datetime library 
    name= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day = datetime.datetime.strptime(row[0], '%Y%m%d').weekday()
    name_day=name[day]
    
    rows= cursor.execute(sql, (int(row[0]), row[1], row[2], row[3], row[4], quarter, name_day))
    count=count+1
    if count % 10 == 0:
        print("Loaded " +str(count)+ " rows")

cnxn.commit()
time.close()


print("Done time")
print("Loaded " +str(count)+ " rows in Time \n")



print("\n \n")
print("done all the dimensions loading")

#CPU CASE
#-----------------------------

#open connection
cnxn = pyodbc.connect(connectionString)
cursor = cnxn.cursor()

#import file and prepare it
ifile='D:file_pro/factCPU.csv'
cpuf=open(ifile)
lines = csv.reader(cpuf, delimiter = ',')

#Prepare SQL query
sql ="INSERT INTO Cpu_sales(cpu_code,time_code,geo_code,vendor_code,sales_usd,sales_currency) VALUES(?,?,?,?,?,?)"

print("Start the loading in Cpu_sales")
count=0

#Start the loading
for row in lines:
    rows= cursor.execute(sql, int(float(row[1])), int(row[2]), int(row[3]), int(row[4]), float(row[5]), float(row[6]))
    count=count+1
    
    #If for controll the number of rows loaded and the row number if there is an error
    if count%10==0:
        print("Loaded " +str(count)+ " rows")
        
#Close connection and file
cnxn.commit()
cpuf.close()

print("Done Cpu_sales")

print("Loaded " +str(count)+ " rows in Cpu_sales \n")


#GPU CASE
#-----------------------------

#open connection
cnxn = pyodbc.connect(connectionString)
cursor = cnxn.cursor()

#import file and prepare it
ifile='D:file_pro/factGPU.csv'
gpuf=open(ifile)
lines = csv.reader(gpuf, delimiter = ',')

#Prepare SQL query
sql ="INSERT INTO Gpu_sales(gpu_code,time_code,geo_code,vendor_code,sales_usd,sales_currency) VALUES(?,?,?,?,?,?)"

print("Start the loading in Gpu_sales")
count=0

#Start the loading
for row in lines:
    rows= cursor.execute(sql, int(float(row[1])), int(row[2]), int(row[3]), int(row[4]), float(row[5]), float(row[6]))
    count=count+1
    
    #If for controll the number of rows loaded and the row number if there is an error
    if count%10==0:
        print("Loaded " +str(count)+ " rows")
   
#Close connection and file
cnxn.commit()
gpuf.close()

print("Done Gpu_sales")

print("Loaded " +str(count)+ " rows in Gpu_sales \n")


#RAM CASE
#-----------------------------

#same procedure, no comment inserted

cnxn = pyodbc.connect(connectionString)
cursor = cnxn.cursor()

ifile='D:file_pro/factRAM.csv'
ramf=open(ifile)
lines = csv.reader(ramf, delimiter = ',')

sql ="INSERT INTO Ram_sales(Ram_code,time_code,geo_code,vendor_code,sales_usd,sales_currency) VALUES(?,?,?,?,?,?)"

print("Start the loading in Ram_sales")
count=0

for row in lines:
    rows= cursor.execute(sql, int(float(row[1])), int(row[2]), int(row[3]), int(row[4]), float(row[5]), float(row[6]))
    count=count+1
    
    if count%10==0:
        print("Loaded " +str(count)+ " rows")
        
cnxn.commit()
ramf.close()

print("Done Ram_sales")

print("Loaded " +str(count)+ " rows in Ram_sales \n")

print("\n \n")
print("done all the fact loading")

print("\n \n")
print("done all the loading")
