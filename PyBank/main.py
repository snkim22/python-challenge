
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period


import os
import csv

# print(os.getcwd())

file_path = r'C:\Users\SarahKim\UCB\Module_Challenge\python-challenge\python-challenge\PyBank\Resources\budget_data.csv'

def print_financial_anaylysis():
    with open(file_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)
        data = list(csvreader)

    total_months = len(data)
    total_change = 0
    net_changes = []
    months = []

    for i in range(total_months):
        month = data[i][0]
        change = int(data[i][1])
        months.append(month)
        total_change += change
        
        if i > 0:
            net_change = change - int(data[i-1][1])
            net_changes.append(net_change)

    total_net_change = sum(net_changes)
    ave_change = total_net_change / len(net_changes)
    max_inc = max(net_changes)
    max_inc_month = months[net_changes.index(max_inc)+1]
    max_dec = min(net_changes)
    max_dec_month = months[net_changes.index(max_dec)+1]

    print('Finanical Analysis')
    print('----------------------------')
    print(f'Total Months: {total_months}')
    print(f'Total: ${total_change}')
    print(f'Average Change: ${ave_change:.2f}')
    print(f'Greatest Increase in Profits: {max_inc_month} (${max_inc})')
    print(f'Greatest Decrease in Profits: {max_dec_month} (${max_dec})')


print_financial_anaylysis()
