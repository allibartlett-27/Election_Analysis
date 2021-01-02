#The data we need to retrieve
#1. Total # of votes cast
#2. A complete list of candidates who received votes
#3. Total # of votes each candidate received
#4. % of votes each candidate won
#5. The winner of the election based on popular vote
import csv
import os
#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_load) as election_data:
    #To DO: read and analyze the data here.
    file_reader = csv.reader(election_data)
    
    headers = next(file_reader)
    print(headers)
    
    
