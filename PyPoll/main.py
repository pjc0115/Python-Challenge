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
 
#count = 0
#Tcount = 0

# Opern csv file with a comma delimiter 
with open(poll_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter =",")
    csv_header = next(csv_reader)
    
    #Set for loop
    for row in csv_reader:
        #count =+ count   #count the number of votes
        
        num_votes.append(row[0])  
        tot_count = len(num_votes)
       
        
        candidates.append(row[2])
    

      
  
    # Output to Terminal
    
    print("-------------------------")
    print("-------------------------")
    print("ELECTION ANALYSIS")
    print("-------------------------")
    print("TOTAL VOTES: " + str(tot_count)) 
   
    
    # Output to .txt file
    
with open('Election_Analysis.txt', "w") as textfile:  #Write to Election_Analysis.txt
    textfile.write("-------------------------\n")  #newline \n
    textfile.write("-------------------------\n")
    textfile.write("ELECTION ANALYSIS" + "\n")
    textfile.write("-------------------------\n")
    textfile.write("TOTAL VOTES: " + str(tot_count) + "\n")  
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    