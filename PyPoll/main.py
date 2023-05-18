#import module/s
import os
import csv

#link the csv file to the main.py
csvpath = os.path.join("..", "Resources", "election_data.csv")

#create a variable to read/access the csv opened file
with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#skips header
    next(csvfile)

#setup list to hold value and reference
    votes_tally = [0,0,0]
    candidate_list = ["Charles Casper Stockham","Diana DeGette","Raymon Anthony Doane"]

#create a loop something like a tally ticker
    for rows in csvreader:
        votes_tally[candidate_list.index(rows[2])] += 1

#output result
print ("\nElection Results")
print ("\n----------------------------\n")
print (f"Total Votes: {sum(votes_tally)}")
print ("\n----------------------------\n")

for candidate in range(len(candidate_list)):
    print (f"{candidate_list[candidate]}: {(votes_tally[candidate]/sum(votes_tally)):.3%} ({votes_tally[candidate]})")

print ("\n----------------------------\n")
print (f"Winner: {candidate_list[votes_tally.index(max(votes_tally))]}")
print ("\n----------------------------\n")


#this line exports the result to the Analysis folder
writeResult = open ("../Analysis/Output Result.txt","w+")
writeResult.write ("\nElection Results")
writeResult.write ("\n----------------------------\n")
writeResult.write (f"Total Votes: {sum(votes_tally)}")
writeResult.write ("\n----------------------------\n")

for candidate in range(len(candidate_list)):
    writeResult.write (f"{candidate_list[candidate]}: {(votes_tally[candidate]/sum(votes_tally)):.3%} ({votes_tally[candidate]})\n")

writeResult.write ("\n----------------------------\n")
writeResult.write (f"Winner: {candidate_list[votes_tally.index(max(votes_tally))]}")
writeResult.write ("\n----------------------------\n")
writeResult.close
csvfile.close()
