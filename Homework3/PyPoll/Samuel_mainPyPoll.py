# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 16:53:34 2019

@author: Twilight Navigator
"""


import csv
import os
import string

csvpath = "election_data.csv"

voter_id_list=[]
winning_votes=0
voter_id_tally=0

with open(csvpath, "r") as datafile:
    reader = csv.reader(datafile)
    header = next(reader)
    election_data = csv.reader(datafile, delimiter=',')
   
    candidates_list=[] 
    for row in election_data:  
        voter_id_tally+=1
        candidates_list.append(row[2])
        
    candidates_list_unique = list(set(candidates_list))
    name_count= {}
    percentage_vote = {}
 
 
    for name in candidates_list_unique:
        count= candidates_list.count(name)
        name_count[name]=count
        percentage_vote[name] = (round(((name_count[name])/voter_id_tally) *100,2))
        #have it print out each canidate on a seperate row
        #have it print the canidates in order from highest percentage to\
        #lowest percentage
        #for percent in percentage_vote:
           # sort= percentage_vote.sort(name)
            
        #print(name)
        
    for n in name_count:
        if(name_count[n]> winning_votes):
            winning_votes= name_count[n]
            winner=n

#print(name_count)              
#print(percentage_vote)
#print(winner)
tooley_percent= percentage_vote["O'Tooley"] 
tooley_count= name_count["O'Tooley"]
#print(tooley_percent)

print("Election Results")
print("-------------------------")
print(f'{candidates_list_unique[3]}: {percentage_vote["Khan"]}% ({name_count["Khan"]})')
print(f'{candidates_list_unique[2]}: {percentage_vote["Correy"]}% ({name_count["Correy"]})')
print(f'{candidates_list_unique[0]}: {percentage_vote["Li"]}% ({name_count["Li"]})')
print(f'{candidates_list_unique[1]}: {tooley_percent}% ({tooley_count})')
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")

electionoutput_file = os.path.join("election_data.txt")

with open(electionoutput_file, "w", newline="") as textfile:
   writer = textfile.write(Summary)