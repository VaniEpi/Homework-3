import os
import csv

budget_data = os.path.join("03-Python", "Instructions" , "PyBank" ,"Resources" , "budget_data.csv")

# list all the variables 
total_months = 0

change_proloss=[]
#inc_proloss
#dec_proloss
total_proloss = []

# Open and read csv
with open(budget_data, newline="") as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   
    
   csv_header = next(csvreader)
   #print(f"CSV HEADER: {csv_header}")
   
   
   for row in csvreader:
      #print(row)

      total_proloss.append(float(row[1]))
       
      # Track the totals number of months
      total_months = total_months + 1
      print(total_months)
      
   print("Total profits and losses: $", sum(total_proloss))
      
      
     # Calculate Average change

   for y in range(1, len(total_proloss)):
      change_proloss.append(total_proloss[y] - total_proloss[y-1])
      avg_change_proloss = sum(change_proloss)/len(change_proloss)
   print(avg_change_proloss)

      # Calculate Greatest increase
   max_change = max(change_proloss)
   print(max_change)
      # Calculate greatest decrease
   min_change = min(change_proloss)
   print(min_change)
    #month = str(budget_data[0])
    #profit_losses = int(budget_data[1])

    #count = month.count('January 1, 2010')
    #print('the count of Jan-10 is:', count)   \n to print to new line in text file 