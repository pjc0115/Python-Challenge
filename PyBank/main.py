# Import libraries for os and csv

import os
import csv

# Create path to csv file called Budget_Data.csv
# revenue_csv = "..\Resources\budget_data.csv"  # Relative path not quite working locally for me.  Default to os.path.join

revenue_csv = os.path.join('Resources', 'budget_data.csv')  # Use os.path.join function to concatenate directory with csv file

# Use lists to store data 

month = []
profit = []
monthly_changes = []
date = []

# Initialize variables
 
count = 0
tot_profit = 0
tot_change_in_profits = 0
starting_profit = 0
monthly_change_profits = 0

# Open the CSV and set up iterator

with open(revenue_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
   
     # Set loop
    for row in csvreader:
      
      # Append period data to list  
      month.append(row[0])  
      tot_month = len(month)
    
      # Will need it when collecting the greatest increase and decrease in profits
      #date.append(row[0])

      # Append profit/losses data to list
      profit.append(row[1])
      tot_profit += int(row[1])                   
    
      # Setup to calc average change in profits
      final_profit = int(row[1])
          
      monthly_change_profits = final_profit - starting_profit
      #print(tot_profit,  final_profit,  starting_profit)
           
      # Calc average
      avg_change_profits = (monthly_change_profits/tot_month)
  
    # Output to Terminal
    
    print("-------------------------")
    print("-------------------------")
    print("FINANCIAL ANALYSIS")
    print("-------------------------")
    print("TOTAL MONTHS: " + str(tot_month)) 
    print("TOTAL PROFIT: " + "$" + str(tot_profit))
    print("CHANGE-AVERAGE: " + "$" + str(int(avg_change_profits)))
    
    
    # Output to .txt file
    
with open('Fin_Analysis.txt', "w") as textfile:  #Write to Fin_Analysis.txt
    textfile.write("-------------------------\n")  #newline \n
    textfile.write("-------------------------\n")
    textfile.write("FINANCIAL ANALYSIS" + "\n")
    textfile.write("-------------------------\n")
    textfile.write("TOTAL MONTHS: " + str(tot_month) + "\n")  
    textfile.write("TOTAL PROFIT: " + "$" + str(tot_profit) + "\n")
    textfile.write("CHANGE-AVERAGE: " + "$" + str(int(avg_change_profits)))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    