# The data we need to retrieve
#1. The total number of votes cast
#2 A complete list of condidates who received votes
#3 The percentage of votes each candidate won
#4 The total number of votes each condidate won
#5 The winner of the election based on popular vote
# import csv
# import os

# file_to_load = os.path.join('Resources', 'election_results.csv')
# file_to_save = os.path.join("analysis/election_results.txt")
# with open(file_to_load) as election_data:
#     reader = csv.reader(election_data)
#     header = next(reader)
#     print(header)
# election_data = open(file_to_load, 'r')
# election_data.close()
# with open(file_to_save, "w") as text_file:
#     data_tosave = 'next(reader)'
#     text_file.write(data_tosave)
#     print(election_data)
# import os
# dir (os)
# file_to_load = os.path.join("Resources", "election_results.csv")
# with open(file_to_load) as election_data:
#     print(election_data)
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# open(file_to_save, "w")
# open(analysis), "w")
#     file_to_save = os.path.join("analysis","election_analysis.txt")
#     outfile = open(file_to_save, "w")
#     outfile.write("Hello World")
#     outfile.close()
# with open(file_to_save, "w") as txt_file:
#     txt_file.write("Hello World")

import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")
print(file_to_load)
file_to_save = os.path.join("analysis", "election_analysis.txt")
# 1. Initialize a total vote counter.
total_votes = 0
candidates_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # 
 
    # for row in file_reader:
    #     print(row[0])

    headers = next(file_reader)
    print(headers)
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
        # Print the candidate name from each row
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidates_options:
            # Add it to the list of candidates.
            candidates_options.append(candidate_name)
            # 3. Print the total votes.
            # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
# Print the candidate vote dictionary.
# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    # To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    # Determine winning vote count and candidate
    # 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If true then set winning_count = votes and winning_percent =
        # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # 3. Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name
winning_candidate_summary = (
f"-------------------------\n"
f"Winner: {winning_candidate}\n"
f"Winning Vote Count: {winning_count:,}\n"
f"Winning Percentage: {winning_percentage:.1f}%\n"
f"-------------------------\n")
print(winning_candidate_summary)

print(candidate_votes)



