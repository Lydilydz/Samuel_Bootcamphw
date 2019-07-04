# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 16:47:40 2019

@author: Twilight Navigator
"""

"""Homework """
# import moduel 
import csv
import os

#set path for file
csvpath =os.path.join("budget_data.csv")
month_tally = 0
profit_losses= 0
previous_profit= 0
profit_list=[]
month_list=[]

with open(csvpath, "r") as datafile:
    reader = csv.reader(datafile)
#The total number of months included in the dataset"""

    header = next(reader)
   
    for row in reader:
        month_tally += 1
        profit_losses += float(row[1])
        current_profit= float(row[1])
        if previous_profit != 0:
            change_profit= float(current_profit) - float(previous_profit )
            profit_list.append(change_profit)
            month_list.append(row[0])
        previous_profit = current_profit
        
        #print(profit_list)
        
    average_change= round(sum(profit_list)/ month_tally,2)
    #print(average_change)
    max_profit= max(profit_list)
    #(max_profit)
    max_month= month_list[profit_list.index(max_profit)]
    #print (max_month)
    min_profit= min(profit_list)
    #print(min_profit)
    min_month= month_list[profit_list.index(min_profit)]
    #print(min_month)


#print  ("Financial Analysis")
#print ("----------------------------")
#
#print("Total Months: " + str(month_tally))
#
##The net total amount of "Profit/Losses" over the entire period"""
#
#print("Total: " + "$" +str(profit_losses))

#The average of the changes in "Profit/Losses" over the entire period"""

#print("Average Change: " + str(average_change))

#The greatest increase in profits (date and amount) over the entire period"""

#print("Greatest Increase in Profits: " +str(max_month) +" $" + str(max_profit))

#The greatest decrease in losses (date and amount) over the entire period"""

#print("Greatest Decrease in Profits: " + str(min_month) + " $" + str(min_profit ))

#output_path=os.path.join ("output","new.txt")
#with open(out_path, 'w', newline= '') as 

Summary =(f'Financial Analysis\n'
   f'----------------------------\n'
   f'Total Months: {month_tally}\n'
   f'Total: ${profit_losses}\n'
   f'Average Change:${average_change}\n'
   f'Greatest Increase in Profits: {max_month} (${max_profit})\n'
   f'Greatest decrease in Profits: {min_month} (${min_profit})\n')
#print  ("Financial Analysis")
#print ("----------------------------")
print(Summary)


bankoutput_file = os.path.join("bank_summary.txt")

with open(bankoutput_file, "w") as textfile:
   writer = textfile.write(Summary)
