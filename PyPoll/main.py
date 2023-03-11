# Module 3 - Python Challenge - PyPoll Analysis - Jalaj Sharma

# Importing python modules
import csv
import os

# Declaring the file path for the raw data input
poll_data_path = os.path.join("Resources", "election_data.csv")
# Declaring the file path for the analysis text output
text_output_path = os.path.join("analysis", "text_output.txt")

# List for recording the candidate names
candidate_names = []

# Open the file usng the file path and read the data by setting ',' as the delimiter
with open(poll_data_path) as input_data:
    read_data = csv.reader(input_data, delimiter=',')        

    # Record the header and move onto the next row/line
    read_data_header = next(read_data)

    # With the header out of the way, start reading one row at a time
    # Using list comprehension, add all the names voted to an empty list
    # With this list of names, all required information can be obtained
    candidate_names = [row[2] for row in read_data]

total_votes = len(candidate_names)

# With the candidates voted list prepared, remove all duplicates.
# This also allows for tackling any number of unique candidates, not just three
# https://www.w3schools.com/python/python_howto_remove_duplicates.asp
candidate_names_no_duplicates = list(dict.fromkeys(candidate_names))

# Initialising list to capture the number of votes for the corresponding candidates
candidate_votes = [0] * len(candidate_names_no_duplicates)
candidate_votes_percent = [0] * len(candidate_names_no_duplicates)
   
# Print the data to the terminal
print("\nElection Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")

# Use a loop to go through the unique candidates lists
for i in range(len(candidate_names_no_duplicates)):

    # Count the number of occurrences/votes of the unique candidates in the raw voted candidates list
    # https://www.programiz.com/python-programming/methods/list/count
    candidate_votes[i] = candidate_names.count(candidate_names_no_duplicates[i])

    # Use the number of votes to compute the percentage of votes
    candidate_votes_percent[i] = round(((candidate_votes[i] / total_votes) * 100), 3)

    # Print the data to the terminal
    print(f"{candidate_names_no_duplicates[i]}: {candidate_votes_percent[i]}% ({candidate_votes[i]})")
print("----------------------------")

# Using the MAX function, find the most voted candidate and used its index to identify the candidate
winner_index = candidate_votes.index(max(candidate_votes))

# Print the data to the terminal
print(f"Winner: {candidate_names_no_duplicates[winner_index]}")
print("----------------------------")

# Open/create the file usng the file path and write into the file
with open(text_output_path, "w") as output_text:
    # Use the .write instruction for writing text into the file
    output_text.write("Election Results")
    output_text.write("\n----------------------------")
    output_text.write(f"\nTotal Votes: {total_votes}")
    output_text.write("\n----------------------------")

    for i in range(len(candidate_names_no_duplicates)):
        output_text.write(f"\n{candidate_names_no_duplicates[i]}: {candidate_votes_percent[i]}% ({candidate_votes[i]})")
    
    output_text.write("\n----------------------------")
    output_text.write(f"\nWinner: {candidate_names_no_duplicates[winner_index]}")
    output_text.write("\n----------------------------")