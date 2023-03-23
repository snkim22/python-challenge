import pandas as pd

# define file path and read in the CSV (pd.read_csv stores header row)

data_file = 'Resources/election_data.csv'
election_df = pd.read_csv(data_file)

# Since each row is a unique Ballot ID use len to find total number of votes cast

total_votes_cast = len(election_df)

print('Election Results')
print('-------------------------')
print('Total Votes:'+ str(total_votes_cast))
print('-------------------------')

# select the 'Candidate' column in the df and use .value_counts to tally each time a unique candidate appears
# use .sort_index to sort results alphabetically (to match example provided)

candidate_votes = election_df['Candidate'].value_counts().sort_index()

# initially set the variables max_votes as 0 and winner blank
# use .items to set candidate as keys and votes as values

max_votes = 0
winner = ''

# loop through to tally votes per candidate and replace max_votes until we find the winner
for candidate, votes in candidate_votes.items():
    percent = votes/total_votes_cast *100
    print(f'{candidate}: {percent:.3f}% ({votes})')
    if votes > max_votes:
        max_votes = votes
        winner = candidate

print('-------------------------')
print('Winner:' + str(winner))
print('-------------------------')

# define the path for output file, open, and write in the analysis (use \n to print each output in new line)
output_file = 'Analysis/output.txt'
with open(output_file, 'w') as f:
    print('Election Results',file=f)
    print('-------------------------',file=f)
    print('Total Votes:'+ str(total_votes_cast),file=f)
    print('-------------------------',file=f)
    for candidate, votes in candidate_votes.items():
        percent = votes/total_votes_cast *100
        print(f'{candidate}: {percent:.3f}% ({votes})',file=f)
    print('-------------------------',file=f)
    print('Winner:'+ str(winner),file=f)
    print('-------------------------',file=f)