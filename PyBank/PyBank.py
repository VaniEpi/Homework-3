import os
import csv

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))

budget_data = os.path.join("Resources" , "budget_data.csv")

# list variables 
total_months = 0
change_proloss = []
total_proloss = []
months = []

# Open and read csv
with open(budget_data, newline="") as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   
   csv_header = next(csvreader)
   print(f"CSV HEADER: {csv_header}")
   
   for row in csvreader:
      print(row)

      months.append(row[0])
      total_proloss.append(float(row[1]))
       
      # Track the totals number of months
      total_months += 1
   
   #print(total_months)
      
   #print("Total profits and losses: $", sum(total_proloss))
      
      
   # Calculate Average change
   # range creates list of incremental numbers from 1 to length of list to use for index to calc change in profit loss
   for i in range(1, len(total_proloss)):
      change_proloss.append(total_proloss[i] - total_proloss[i-1])
   avg_change_proloss = sum(change_proloss) / len(change_proloss)
   # print("Average change in profits and losses: $", avg_change_proloss)

   # Calculate Greatest increase using max function to find greatest value in list
   max_change = max(change_proloss)
   # Find position of maximum change in profit-loss using index
   max_index = change_proloss.index(max_change)
   # Using position, plug into months list to get month associated with max change
   # difference in list size so need to add 1
   inc_month = months[max_index + 1]
   # print("Greatest increase in profits and losses: $", max_change)
     
   # Calculate greatest decrease
   min_change = min(change_proloss)
   min_index = change_proloss.index(min_change)
   dec_month = months[min_index + 1]
   # print("Greatest decrease in profits and losses: $", min_change)

output = """Financial Analysis
----------------------------
Total Months: {months}
Total: ${total:.0f}
Average  Change: ${avg_change:.2f}
Greatest Increase in Profits: {inc_month} (${inc_profit:.0f})
Greatest Decrease in Profits: {dec_month} (${dec_profit:.0f})""".format(
   months=total_months,
   total=sum(total_proloss),
   avg_change=avg_change_proloss,
   inc_month=inc_month,
   inc_profit=max_change,
   dec_month=dec_month,
   dec_profit=min_change
)
print(output)

# write output to a text file 
file = open("PyBank.txt", "w") 
file.write(output)
file.close() 


    
  