# import os and csv
import os
import csv

# variables to be used later
total_votes = 0
candidate_list = []
vote_count = []
percent_votes = []
votes = {}
zipped_lists = []
winner = []

# open csv file and create csv reader
csvpath = os.path.join("/Users/tincho/Desktop/Challenge Reps/Python_Challenge/Pypoll_data/election_data.csv")
with open(csvpath, "r") as csv_file:
    reader = csv.reader(csv_file)
    next(reader, None)
    
    for row in reader:

        # count total votes
        total_votes = total_votes + 1

        #create a dictionary with key = candidate and each row the key is in as an entry
        candidate_names = row[2]
        if candidate_names in votes.keys():
            votes[candidate_names] = votes[candidate_names] + 1
        else:
            votes[candidate_names] = 1

# add keys to candidate list and values to vote count
for key, value in votes.items():
    candidate_list.append(key)
    vote_count.append(value)

# caluclate percentage of votes
for n in vote_count:
    percent_votes.append(round((n/total_votes)*100, 3))

# zip data into candidate/ vote count/ percentage of vote
zipped_lists = list(zip(candidate_list, percent_votes, vote_count))

# find general election winner
for tpl in zipped_lists:
    if max(vote_count) == tpl[2]:
        winner.append(tpl[0])

# create output chart
output = (
    f'\nElection Results\n'
    f'----------------------------------\n'
    f'Total Votes: {total_votes}\n'
    f'----------------------------------\n'
    f'{zipped_lists[0][0]}: {zipped_lists[0][1]}% ({zipped_lists[0][2]})\n'
    f'{zipped_lists[1][0]}: {zipped_lists[1][1]}% ({zipped_lists[1][2]})\n'
    f'{zipped_lists[2][0]}: {zipped_lists[2][1]}% ({zipped_lists[2][2]})\n'
    f'----------------------------------\n'
    f'Winner: {winner[0]}\n'
    f'----------------------------------\n'
)

print(output)

 # create text file
with open("PyPoll_Output", 'w') as txt_file:
    txt_file.write(output)













        





        