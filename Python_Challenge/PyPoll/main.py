#!/usr/local/bin/python

#
#  PyPoll/main.py is to calculate and display text metrics
#  Syntax: python PyPoll/main.py <election_data_csv>
#

#import all required modules here
import csv
import sys

def pollMetrics(pollData_csv):
    with open(pollData_csv, 'r') as fd:
        pollData = csv.DictReader(fd)

        total_votes = 0
        candidate_vote_count = {}
        for row in pollData:
            # count total votes
            total_votes += 1
            if row['Candidate'] in candidate_vote_count:
                candidate_vote_count[row['Candidate']] += 1
            else:
                candidate_vote_count[row['Candidate']] = 1

        print("Election Results")
        print("-------------------------")
        print("Total Votes: " + str(total_votes))
        print("-------------------------")
        
        winner = ""
        highest_votes = 0
        for candidate in candidate_vote_count:
            # find the winner
            if candidate_vote_count[candidate] > highest_votes:
                highest_votes = candidate_vote_count[candidate] 
                winner = candidate
            print("%s: %.2f %s" % (candidate, (candidate_vote_count[candidate]/total_votes) * 100, candidate_vote_count[candidate]))
        print("-------------------------")
        print("Winner: " + winner)
        print("-------------------------")

if __name__ == '__main__':
    pollMetrics(sys.argv[1])
