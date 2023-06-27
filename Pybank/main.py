# import os and csv
import os
import csv

# open csv file and create csv reader
csvpath = os.path.join("/Users/tincho/Desktop/Challenge Reps/Python_Challenge/Pybank_data/budget_data.csv")
with open(csvpath) as dataset:
    csvreader = (csv.reader(dataset, delimiter = ','))

# check if it loads: (FINALLY IT DOES JESUS) print(csvreader)
# read header and skip first row
    csv_header = next(csvreader)

#    for row in csvreader: (edit* it works)
#        print(row)        (edit* it works)


# create the sum of months
    ## for some reason this isnt working. will debug later 
    total_months = 0
    for row in csvreader(dataset):
        total_months += int(row[1])
    print(total_months)


    
    
        