import os
import csv


election_data = os.path.join("03-Python" , "Instructions" , "PyPoll" , "Resources" , "election_data.csv" )

# create dictionary to hold data on candidates and the number of votes
totalvotes = 0
candidates = {}

#open and read election data csv file
with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
   
    for row in csvreader:
        #print(row)
        
        totalvotes = totalvotes + 1

    #populate candidates dictionary
        if row[2] in candidates:
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

    highestvotes = 0
    winner = ""

#Calculate percent votes for each candidate and print the candidates name and their percentage of votes 
#rounded to 2 decimal places
    for candidate in candidates:
        percentvote = (candidates[candidate] / totalvotes) * 100
        print(f"{candidate}: {round(percentvote, 3)}% ({candidates[candidate]})")
        

        if candidates[candidate] > highestvotes:
            highestvotes = candidates[candidate]
            winner = candidate

    print(f"Winner: {winner}")

