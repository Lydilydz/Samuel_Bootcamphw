# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 16:53:34 2019

@author: Twilight Navigator
"""

# import moduel 
import csv
import os
import string

#candidates = csvpath.load_dataset('Candidate')
#candidates.name

#set path for file
csvpath = "election_data.csv"
#df= pd.csvpath([coulmn])
#csv.groupby(['Candidate'])
country_list=[]
voter_id_list=[]
candidate_list=[] 
voter_id_tally=0

#give me a list of the candidates
#tell me how many votes each candidate has 
#string.count(value, start, end)



with open(csvpath, "r") as datafile:
    reader = csv.reader(datafile)
    header = next(reader)
   
    for row in reader:  
        voter_id_tally+=1
      


#csv.head
#print(voter_id_tally)
#print (canidiate_list)  
print("Election Results")
print("-------------------------")

 
#Total Votes: 3521001
print("Total Votes: " +str(voter_id_tally)) 


print("-------------------------")


  
 
# Khan: 63.000% (2218231)
print("Khan: " +""+ "")
 

#Correy: 20.000% (704200)
print("Correy: " + "" +"")
  

#Li: 14.000% (492940)
print("Li: " +""+"")


#O'Tooley: 3.000% (105630)
print("O'Tooley: " +""+"") 
print("-------------------------")

#Winner: Khan
print("Winner:" "")

print("-------------------------")
