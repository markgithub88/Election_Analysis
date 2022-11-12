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
file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # for row in file_reader:
    #     print(row)
 
    # for row in file_reader:
    #     print(row[0])

    headers = next(file_reader)
    print(headers)
    
