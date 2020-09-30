#@temkuh
import os
import csv
import operator
from collections import defaultdict

#Create your 2 dictionaries to store data
candidate_dict = {}
votes_dict = {}

#replace path here:
#path = "Resources","election_data.csv"


#with open("/Users/atemkuh/Documents/GitHub/RUT-SOM-DATA-PT-09-2020-U-C/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv") as csvfile:
with open("Resources","election_data.csv") as csvfile:
    
    #Read the csv file
    readCSV = csv.reader(csvfile, delimiter=',')
    
    #Create dates and profits arrays
    vote_ids = []
    counties = []
    candidates = []
    
    #loop the csv file to read its data
    for row in readCSV:
        vote_id = row[0]
        county = row[1]
        candidate = row[2]
        
        #Store dates and profits into their respective arrays
        vote_ids.append(vote_id)
        counties.append(county)
        candidates.append(candidate)
    
#List of unique candidates (no duplicates)
unique_candidates = list(set(candidates))

#Initialize votes_dict
for a in unique_candidates:
    votes_dict[a] = 0    
print('======================================================')
print('|                  Election Results                  |')
print('======================================================')                
#Populate the dictionary with candites keys and increment their votes
for t in range (1, len(vote_ids)):
    
    for z in range(0, len(unique_candidates)):
        if candidates[t] in unique_candidates[z]:
            votes_dict[unique_candidates[z]] += 1            
            
    
#Get the count of total votes
total_voters = len(vote_ids)

print("Total Votes: %s" %(total_voters))
print('|======================================================|')  

#Print the results in numbers of votes
for i in votes_dict:
    if i not in "Candidate":
        print(i, votes_dict[i])
print('|======================================================|')  


#Print the results in % 
for i in votes_dict:
    if i not in "Candidate":
        print(i, (votes_dict[i]/total_voters)*100)
      

#output text file

output_file = os.path.join("election_results.txt")
with open(output_file, "w", newline="") as datafile:
    datafile.write('======================================================\n')
    datafile.write('|                  Election Results                  |\n')
    datafile.write('======================================================\n')
    datafile.write("Total Votes: %s" %(total_voters))
    datafile.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

