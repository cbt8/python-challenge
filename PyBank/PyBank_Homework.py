
# coding: utf-8

# In[1]:


import csv

csvpath = ("./Resources/budget_data.csv")

month = 0
profit_losses = 0
date_list = []
profit_list = []

with open(csvpath, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)
    print(f"{csv_header}")

    for row in csvreader:
        month += 1
        date_list.append(row[0])
        profit_list.append(int(row[1]))
        
        
    for i in range(len(profit_list)):
        profit_losses += int(profit_list[i])
        

    best_month = profit_list.index(max(profit_list))
    worst_month = profit_list.index(min(profit_list))
    
    print(f"Financial Analysis \n----------------------------\nTotal Months: {month}\nTotal Profit: ${profit_losses:,d}\nAverage  Change: ${int(round(profit_losses/month,2)):,d}\nGreatest Increase in Profits: {date_list[best_month]} ${profit_list[best_month]:,d}\nGreatest Decrease in Profits: {date_list[worst_month]} ${profit_list[worst_month]:,d}")
    
    
    
    

