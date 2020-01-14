import os
import csv

election_data = os.path.join("Resources" , "election_data.csv" )

# create dictionary to hold data on candidates and the number of votes
total_votes = 0
output = ""
candidates = {}

#open and read election data csv file
with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    # print(f"CSV HEADER: {csv_header}")

    for row in csvreader:
        total_votes = total_votes + 1
    
        # populate candidates dictionary
        # if candidate name is already a key in dictionary, then add 1
        # if candidate name is not in dictionary, then create new key-value pair
        if row[2] in candidates:
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

    # print(total_votes)
    # output = output + "Election Results\n" (output was previously "")
    output += "Election Results\n"
    output += "-------------------------\n"
    output += "Total Votes: {total_votes}\n".format(
        total_votes=total_votes
    )
    output += "-------------------------\n"


    highest_votes = 0
    winner = ""

#Calculate percent votes for each candidate and print the candidates name and their percentage of votes 
#rounded to 2 decimal places
    for candidate in sorted(candidates, key=candidates.get, reverse=True):
        percent_vote = (candidates[candidate] / total_votes) * 100

        output += "{name}: {percent:.3f}% ({total})\n".format(
            name=candidate,
            percent=percent_vote,
            total=candidates[candidate]
        )

        if candidates[candidate] > highest_votes:
            highest_votes = candidates[candidate]
            winner = candidate

    output += "-------------------------\n"
    output += "Winner: {winner}\n".format(
        winner=winner
    )
    output += "-------------------------\n"


print(output)

# write output to a text file 
file = open("PyPoll.txt", "w") 
file.write(output)
file.close() 

"""
text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  """