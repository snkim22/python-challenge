# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

import os
import csv

# print(os.getcwd())

file_path = r'C:\Users\SarahKim\UCB\Module_Challenge\python-challenge\python-challenge\PyPoll\Resources\election_data.csv'

def print_election_results():
    with open(file_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)
        