# Import libraries for os and csv

import os
import csv

# Create path to csv file called Budget_Data.csv
# revenue_csv = "..\Resources\budget_data.csv"  # Relative path not quite working locally for me.  Default to os.path.join

poll_csv = os.path.join('Resources', 'election_data.csv')  # Use os.path.join function to concatenate directory with csv file

# Use lists to store data for candidates, percentage fo votes, number of votes, and popular votes

candidates = []
vote_percentage = []
num_votes = []
popular_votes = []

# Initialize variables
 
count = 0


      
  
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    