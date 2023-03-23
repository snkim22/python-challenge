
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period

import csv

# define file path 
file_path = "Resources/budget_data.csv"

# define function to print our key findings
# open the CSV file, create reader object, and skip header row
# set the data as a list
def print_financial_anaylysis():
    with open(file_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)
        data = list(csvreader)

# each row is unique month so use len to find total months
    total_months = len(data)

# first, define variables to calculate net change (profit/losses)
    total_change = 0
    net_changes = []
    months = []

# loop though list to find the profit/losses from each row and add to the list
# find total changes over entire period by adding profit/losses in each row to total_change
    for i in range(total_months):
        month = data[i][0]
        change = int(data[i][1])
        months.append(month)
        total_change += change

# starting from the second row of data
# minus previous month's pofit/losses from current month and add to list of net_changes
        if i > 0:
            net_change = change - int(data[i-1][1])
            net_changes.append(net_change)

# sum net changes to find total net change and find the average
    total_net_change = sum(net_changes)
    ave_change = total_net_change / len(net_changes)

# find the max and min net_changes and use index to identify the corresponding month
# +1 is used because net_changes starts on the second month 
    max_inc = max(net_changes)
    max_inc_month = months[net_changes.index(max_inc)+1]
    max_dec = min(net_changes)
    max_dec_month = months[net_changes.index(max_dec)+1]

# print each piece of our anaylsis
    print('Finanical Analysis')
    print('----------------------------')
    print(f'Total Months: {total_months}')
    print(f'Total: ${total_change}')
    print(f'Average Change: ${ave_change:.2f}')
    print(f'Greatest Increase in Profits: {max_inc_month} (${max_inc})')
    print(f'Greatest Decrease in Profits: {max_dec_month} (${max_dec})')

# define the path for output file, open, and write in the analysis
    output_file = "Analysis/output.txt"
    with open(output_file, 'w') as f:
        print('Finanical Analysis',file=f)
        print('----------------------------',file=f)
        print(f'Total Months: {total_months}',file=f)
        print(f'Total: ${total_change}',file=f)
        print(f'Average Change: ${ave_change:.2f}',file=f)
        print(f'Greatest Increase in Profits: {max_inc_month} (${max_inc})',file=f)
        print(f'Greatest Decrease in Profits: {max_dec_month} (${max_dec})',file=f)

# finally, call the function
print_financial_anaylysis()
