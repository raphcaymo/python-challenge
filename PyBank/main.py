#import necessary modules
import os
import csv

#link the csv file to the main.py
csvpath = os.path.join("..", "Resources", "budget_data.csv")

#create a variable to read/access the csv file opened
with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#this line moves the reader to the next line
    next(csvfile)

#pre setting of variables that will be used in the loop and result
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
#total month will increment as the rows index goes by
        total_month = int(total_month + 1)

#total month keeps adding each cells until it reaches the end of the rows
        total += int(rows[1])   

#calculation of average Change, greatest increase and decrease in Profit together with the month 
        prevRow = tempInt1
        if prevRow != 0:
            tempInt2 = int(rows[1]) - prevRow
            change.append(tempInt2)
            monthChange.append(rows[0])
            tempInt1 = int(rows[1])
        else:
            tempInt1 = int(rows[1])
#
#the list change and monthChange are very helpful in the incoming code as they are capturing data to access in solving 
#the last two items.
#


    print (f"")

    #This is to print the result to the terminal
    print ("Financial Analysis ")
    print ("--------------------------")
    print (f"Total Month: {total_month}")
    print (f"Total: ${total}")
    print (f"Average Change: ${(sum(change)/len(change)):.2f}")
    print(f"Greatest increase in Profit {monthChange[change.index(max(change))]} $({max(change)})")
    print(f"Greatest decrease in Profit {monthChange[change.index(min(change))]} $({min(change)})")


#this line exports the result to the Analysis folder
    writeResult = open ("../Analysis/Output Result.txt","w+")
    writeResult.write ("Financial Analysis \n")
    writeResult.write ("--------------------------\n")
    writeResult.write (f"Total Month: {total_month}\n")
    writeResult.write (f"Total: ${total}\n")
    writeResult.write (f"Average Change: ${(sum(change)/len(change)):.2f}\n")
    writeResult.write (f"Greatest increase in Profit {monthChange[change.index(max(change))]} $({max(change)})\n")
    writeResult.write (f"Greatest increase in Profit {monthChange[change.index(min(change))]} $({min(change)})\n")
    writeResult.close()

#practice closing the csvfile when done coding
    csvfile.close()

    