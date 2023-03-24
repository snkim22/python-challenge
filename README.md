# Python Challenge

## PyBank

![Project Image](revenue-per-lead.png)

#### A python script to analyze the financial records of a company 
- Step 1: Each row in the data set represents a unique month, the length of the dataset (after the header row) is used to find the total number of months included in the dataset.
- Step 2: Created a total_change variable, initially set to 0, and loop through the dataset using the += operatior to find the net total amount of "Profit/Losses" over the entire period.
- Step 3: Use lists to loop through the data, starting from the second row, subtract previous month's "Profit/Losses' from the current month and appended to list of net_changes (making sure to cast as int) to find the changes in "Profit/Losses" over the entire period. The average of these changes is calculated by summing the net changes to find total net change and dividing that by the length.
- Step 3: The max() and min() functions as well as.index() were used to to find the greatest increase in profits and greatest decrease in profits over the entire period (date and amount) and then match the corresponding month.
- Step 4: Finally, the output file path was defined, opened, and the final analysis was written into the file. The print_financial_analysis function was called to print the results to the terminal.

## PyPoll

![Project Image](Vote_counting.png)

#### A python script to help a small, rural town modernize its vote-counting process

- Step 1: After setting the dataset as a dataframe, the len() of the dataframe was used to find the total number of votes cast (each row represents a unique ballot ID)
- Step 2: Utilized the .value.counts() function of the 'Candidate' series to find each unique candidate name.
- Step 3: After defining variables for max votes and the winner (initially 0 and a blank string), loop throug the data to calculate the percent per candiate.
- Step 4: While looping through the df, tally the number of votes per candidate and replace the max votes variable with the most popular candidate.
- Step 5: Print the election results in the terminal and write the results into a new text file after defining the path. 
