import time, sys
import csv
import os
import glob
import random
import datetime
os.system('modprobe w1-gpio') 
os.system('modprobe w1-therm')
sensors = ["28-0301a27900a7", "28-0301a2797763", "28-0301a279ac0c", "28-0301a2796df7", "28-0301a279a34f", "28-0301a279c08e"]

filename1 = "temp.csv"
fields = ['Tcin', 'Tcout', 'Thin', 'Thout', 'Tcold', 'Thot']
temperature = [0,0,0,0,0,0]

# writing to csv file 
with open(filename1, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)

# print('Press Ctrl-C to quit.')

def csvWrite(val, fn):
    csvfile = open(fn, 'a', newline='')
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(val)
    csvfile.close()

def startLogs(fn):
    temperature = [0, 0, 0, 0, 0, 0]
    while True:
        for x in range(len(sensors)):
            filename = "/sys/bus/w1/devices/" + sensors[x] + "/w1_slave"
            tempfile = open(filename) 
            temptext = tempfile.read()
            tempfile.close()
            tempcelsius = temptext.split("\n")[1].split(" ")[9]
            temper = float(tempcelsius[2:])
            temperature[x] = temper/1000
        # temperature = [random.random() for _ in range(6)]

        # print(temperature)
        csvWrite(temperature, fn)
        time.sleep(3)

startLogs(filename1)
