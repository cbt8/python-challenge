
# coding: utf-8

# In[32]:


import csv

csvpath = ("./Resources/election_data.csv")

total_votes = 0
candidate_list = []
candidate_set = []

voter_list = []
voter_set = []

#to check if there are duplicate votes

correy = 0
li = 0
otooley = 0
khan = 0


with open(csvpath, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)
    #print(f"{csv_header}")
    
    for row in csvreader:
        total_votes += 1
        candidate_list.append(row[2])
        voter_list.append(row[0])
        
        if row[2]=='Correy':
            correy+=1
                
        elif row[2]=='Li':
            li+=1
        
        elif row[2]=="O'Tooley":
            otooley+=1
        
        elif row[2]=='Khan':
            khan+=1
        
        else: continue
        
        
        
    winner = ""    
    if max(correy, li, otooley, khan) == correy:
        
        winner = "Correy"
    elif max(correy, li, otooley, khan) ==  li:
        
        winner = "Li"
    elif max(correy, li, otooley, khan) ==  otooley:
        
        winner = "O'Tooley"
    elif max(correy, li, otooley, khan) ==  khan:
        
        winner = "Khan"
        
        
        
        
        
    candidate_set = set(candidate_list)    
    voter_set = set(voter_list)
    

    print(candidate_set)
    #print(len(voter_list))
    #print(len(voter_set))      
                
    
    print(f" Election Results\n-------------------------\nTotal Votes: {total_votes}\n------------------------\nKhan: {khan/total_votes:.1%} ({khan})\nCorrey: {correy/total_votes:.1%} ({correy})\nLi: {li/total_votes:.1%} ({li})\nO'Tooley: {otooley/total_votes:.1%} ({otooley})\n-------------------------\nWinner: {winner}\n-------------------------")
    
    
    
    


# In[39]:


import os
import csv

# Specify the file to write to
output_path = os.path.join(".", "Resources", "PyPollResult.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Total Votes', 'Khan', 'Correy', 'Li', "O'Tooley", "Winner"])

    # Write the second row
    csvwriter.writerow([total_votes, khan, correy, li, otooley, winner])


