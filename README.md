# python-challenge

# This challenge consists of two mini projects and Ill walk through my codes

# First project: PyBank

# import necessary modules
import os
import csv

# link the csv file to the main.py
csvpath = os.path.join("..", "Resources", "budget_data.csv")

# create a variable to read/access the csv file opened
with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# this line moves the reader to the next line
    next(csvfile)

# pre setting of variables that will be used in the loop and result
    total_month = 0
    total = 0
    Average_change_total = 0
    tempInt2 = 0
    tempInt1 = 0
    prevRow = 0
    change = []
    monthChange = []

#this loop will search rows in our csv file under resources
    for rows in csvreader:

#
#  this total_month & total calculation is another approach in calculating the total month in the csv file
#   we can also use len() function to calculate number or rows. Same with the total variable that could be written using 
#   sum() function
# 
# total month will increment as the rows index goes by
        total_month = int(total_month + 1)

# total month keeps adding each cells until it reaches the end of the rows
        total += int(rows[1])   

# calculation of average Change, greatest increase and decrease in Profit together with the month 
        prevRow = tempInt1
        if prevRow != 0:
            tempInt2 = int(rows[1]) - prevRow
            change.append(tempInt2)
            monthChange.append(rows[0])
            tempInt1 = int(rows[1])
        else:
            tempInt1 = int(rows[1])
#
# the list change and monthChange are very helpful in the incoming code as they are capturing data to access in solving 
# the last two items.
#


    print (f"")

# This is to print the result to the terminal
    print ("Financial Analysis ")
    print ("--------------------------")
    print (f"Total Month: {total_month}")
    print (f"Total: ${total}")
    print (f"Average Change: ${(sum(change)/len(change)):.2f}")
    print(f"Greatest increase in Profit {monthChange[change.index(max(change))]} $({max(change)})")
    print(f"Greatest decrease in Profit {monthChange[change.index(min(change))]} $({min(change)})")


# this line exports the result to the Analysis folder
    writeResult = open ("../Analysis/Output Result.txt","w+")
    writeResult.write ("Financial Analysis \n")
    writeResult.write ("--------------------------\n")
    writeResult.write (f"Total Month: {total_month}\n")
    writeResult.write (f"Total: ${total}\n")
    writeResult.write (f"Average Change: ${(sum(change)/len(change)):.2f}\n")
    writeResult.write (f"Greatest increase in Profit {monthChange[change.index(max(change))]} $({max(change)})\n")
    writeResult.write (f"Greatest increase in Profit {monthChange[change.index(min(change))]} $({min(change)})\n")
    writeResult.close()

# practice closing the csvfile/s when done coding
    csvfile.close()



# Project 2: PyPoll 
# import module/s
import os
import csv

# link the csv file to the main.py
csvpath = os.path.join("..", "Resources", "election_data.csv")

# create a variable to read/access the csv opened file
with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# skips header
    next(csvfile)

# setup list to hold value and reference
    votes_tally = [0,0,0]
    candidate_list = ["Charles Casper Stockham","Diana DeGette","Raymon Anthony Doane"]

# create a loop something like a tally ticker
    for rows in csvreader:
        votes_tally[candidate_list.index(rows[2])] += 1

# output result
print ("\nElection Results")
print ("\n----------------------------\n")
print (f"Total Votes: {sum(votes_tally)}")
print ("\n----------------------------\n")

for candidate in range(len(candidate_list)):
    print (f"{candidate_list[candidate]}: {(votes_tally[candidate]/sum(votes_tally)):.3%} ({votes_tally[candidate]})")

print ("\n----------------------------\n")
print (f"Winner: {candidate_list[votes_tally.index(max(votes_tally))]}")
print ("\n----------------------------\n")


# this line exports the result to the Analysis folder
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