import os
import csv

election_csv_path = os.path.join("Resources", "election_data.csv")
with open(election_csv_path, newline="") as csvfile:  #open csv file
    csv_reader = csv.reader(csvfile, delimiter=",")

    tot_vote = 0    #init vote counter
    cand_Name = []  #init candidate name list
    cand_Vote = []  #init candidate number of votes list

    next(csv_reader) # skip header row

    # Read through each row of data after the header
    for row in csv_reader:
        tot_vote = tot_vote + 1     #count votes
        if str(row[2]) not in cand_Name :   #if not in list, then new candidate name
            cand_Name.append(str(row[2]))    
            cand_Vote.append(int(1.0))      #first vote
        else:
            ndx = [i for i in range(len(cand_Name)) if cand_Name[i] == str(row[2])] #find index for voted candidate 
            cand_Vote[int(ndx[0])] += 1     #increase vote by 1 for voted candidate

#-------------- sorting by number of votes
# next 3 lines sort candidates by number of votes (in generic case when list not sorted already)
sndx = sorted(range(len(cand_Vote)), reverse=True, key=cand_Vote.__getitem__)  #get indices for sorted case
cand_Name = [cand_Name[i] for i in sndx]    # reorder names per number of votes (using sndx) 
cand_Vote = [cand_Vote[i] for i in sndx]    # reorder votes per number of votes (using sndx) 

perc_Vote = [ (100*item)/(tot_vote) for item in cand_Vote]  #compute vote percentages, a list
win_Cand =cand_Name[0]      #poll winner

#--------------- printing results 
# printing top 4 candidates (generic case), in terminal
print(' ```text Election Results')  
msg = f'Total Votes: {tot_vote} \n\
{cand_Name[0]}: {perc_Vote[0]:.3f}% ({cand_Vote[0]})  {cand_Name[1]}: {perc_Vote[1]:.3f}% ({cand_Vote[1]}) \
 {cand_Name[2]}: {perc_Vote[2]:.3f}% ({cand_Vote[2]})  {cand_Name[3]}: {perc_Vote[3]:.3f}% ({cand_Vote[3]}) \nWinner: {win_Cand}'
print(msg)
print(' ``` ')
# same results to text file 
f = open("resultsPoll.txt", "w")
f.write(msg)
f.close()
