#Add of dependencies.
import csv
import os
#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#1. Intialize a total vote counter.
total_votes = 0
#Candidate Options
candidate_options = []
#Add Dictionaries
candidate_votes = {}
#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #Read the header row
    headers = next(file_reader)
    #Print each row in the CSV file.
    for row in file_reader:
        #2. Add to the total vote count.
        total_votes += 1
        #Print the candidates name from each row.
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            #Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            #Begin tracking the candidate's vote count
            candidate_votes[candidate_name] = 0
        #Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
with open(file_to_save, "w") as txt_file:
    #Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"---------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------\n")
    print(election_results, end="")
    #Save the final vote count to the text file.
    txt_file.write(election_results)
    #Determine the percentage of votes for each candidate by looping through counts
    for candidate_name in candidate_votes:
        #Retrieve vote of a candidate
        votes = candidate_votes[candidate_name]
        #Calclaute percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #Print each candidates, their voter count, and percentage to the #terminal.
        print(candidate_results)
        txt_file.write(candidate_results)
        #Determine winning vote count and candidate
        #Determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #If true then set winning_count = votes and winning_percent = voter percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #Set winning_candidate equal to the candidate's name
            winning_candidate = candidate_name
        winning_candidate_summary = (
            f"-----------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-----------------------\n")
        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)
    
    
