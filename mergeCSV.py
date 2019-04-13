# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 11:40:45 2019

@author: bmusammartanov
"""
#Libraries
import csv
import os

def main():
    """
    Thi is the main program
    """
    location = os.getcwd()
    header = "Date,Time,Voltage,Current,Isolation,Range,SoC,Distance,Fan rpm,Fan Torque,Hyd. Pump rpm,Hyd. Pump Torque,SW Pump rpm,SW Pump Torque,Nozzle,Sidebrushes,WideSweepBrush,TempIGBT-Fan,Fan motor temp, Traction rpm, Traction torque,BMS1 Volts, BMS2 Volts"
    header = header+"\n"

    of ="outFile.csv"
    outFile = open(of, "w")
    outFile.write(header)

    for file in os.listdir(location ):
        try:
             if file.endswith(".csv") and not(file.startswith("outFile")):
                print("...reading {}".format(file))
                fcsv = csv.reader(open(file, newline=''), delimiter=' ', quotechar='|')      
                for row in fcsv:
                    line = ', '.join(row)
                    if line[:4] == "Date":
                        d = line[5:13]
                        dd = d[6:9]+"/"+d[4:6]+"/"+d[:4]
                        next
                    elif line[12] == "*" or line[0] == "*":
                        next
                    elif line[0] == "T":
                        next
                    else:
                        L = dd + "," + line + "\n"
                        outFile.write(L)
        except Exception as e:
            raise e
            print("No CSV files in here!")

    try: 
        print("\nAll files have been merged into: {}".format(of))
        outFile.close()
        
    except Exception as ee:
        raise ee

if __main__ == "main":
    main()
    input("Any key to exit!")
