# Module for reading CSV files
import csv

# Module for getting e 
import math
from math import e

#
# function to calculate new fish weight, given current weight & current temperature
#
def calc_weight (weight_cur, temp_cur):
    # define some constants
    alpha = 0.038
    beta = 0.6667
    tau = 0.08

    # calculate new weight
    weight_new = (alpha * weight_cur**beta * e**(temp_cur * tau)) + weight_cur
    return (weight_new)


# set csvpath
csvpath = 'temperature_series.csv'

# Open CSV file
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # set initial fish weight (arbitrary)
    cur_weight = 1 
    print("Initial fish weight: ", cur_weight)

    # Now read each row of data after the header
    i = 2 # row number
    for row in csvreader: 
        try: 
            # Temperature is 3rd column. Convert it to float.
            temp_cur = float(row[2])
            # Recalculate weight 
            cur_weight = calc_weight(cur_weight, temp_cur)
            i += 1
        except Exception as e:
            print ("Error in reading ", csvpath)
            print ("Row number: ", i)
            print ("Exception: ", e)

    print("Final fish weight: ", round(cur_weight, 6))

