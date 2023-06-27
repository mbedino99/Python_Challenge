# import os and csv
import os
import csv

# open csv file and create csv reader
csvpath = os.path.join("/Users/tincho/Desktop/Challenge Reps/Python_Challenge/Pybank_data/budget_data.csv")
with open(csvpath) as csv_file:
    csvreader = (csv.reader(csv_file, delimiter = ','))

# check if it loads: (FINALLY IT DOES JESUS) print(csvreader)
# read header and skip first row
    csv_header = next(csvreader)

#    for row in csvreader:
#        print(row[1])
            
# iterate throwugh rows and get the sum of months
#    for row in csvreader:
#         total_months = sum(row[0])
#         print(total_months)

# iterate through rows to find net total profit
    for row in csvreader:
        net_profit = sum(int(row[1]))
        print(net_profit)



    


    