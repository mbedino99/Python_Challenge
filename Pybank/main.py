# import os and csv
import os
import csv

# variables to be used later
total_months = 0
old_profit = 0
month_change = []
profit_change_list = []
max_increase = ['', 0]
max_decrease = ['', 10000000000000000000000000000000000000]
total_profit = 0

# open csv file and create csv reader
csvpath = os.path.join("/Users/tincho/Desktop/Challenge Reps/Python_Challenge/PyBank/resources/budget_data.csv")
with open(csvpath) as csv_file:
    reader = csv.DictReader(csv_file)

    for row in reader:

        # calc total months and total profit
        total_months = total_months + 1
        total_profit = total_profit + int(row['Profit/Losses'])

        # calculate profit change
        profit_change = int(row['Profit/Losses']) - old_profit
        old_profit = int(row['Profit/Losses'])
        profit_change_list = profit_change_list + [profit_change]
        month_change = month_change + [row['Date']]

        # calculate max increase 
        if (profit_change > max_increase[1]):
            max_increase[0] = row['Date']
            max_increase[1] = profit_change

        # calculate max decrease
        if (profit_change < max_decrease[1]):
            max_decrease[0] = row['Date']
            max_decrease[1] = profit_change

# calculate average profit change
profit_change = round(sum(profit_change_list) / len(profit_change_list), 2)

# create output chart
output = (
    f'\nFinancial Analysis\n'
    f'--------------------------\n'
    f'Total Months: {total_months}\n'
    f'total Profit: ${total_profit}\n'
    f'Profit change: ${profit_change}\n'
    f'Biggest Increase in Profit: {max_increase[0]} (${max_increase[1]})\n'
    f'Biggest decrease in Profit: {max_decrease[0]} (${max_decrease[1]})\n'
)

print(output)

 # create text file
with open("PyBank_Output", 'w') as txt_file:
    txt_file.write(output)

    
