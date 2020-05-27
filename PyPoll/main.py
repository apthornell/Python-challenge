import os
import csv
#set file import and export paths
electioncsv = os.path.join('..','Resources','election_data.csv')
exportpath= os.path.join('..','Resources','election_results.txt')
#start vote count at 0 and set empty dictionary to take candidate names and vote counts
vote_count=0
cand_unique={}
#opens csv file and moves past header
with open(electioncsv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header=next(csvreader)
    #adds one to vote_count every time it loops through a row, then adds the candidate to dict if it isnt
    #there already by searching for the key, and if it is there it adds one to the value.
    for row in csvreader:
      vote_count += 1
      if row[2] in cand_unique.keys():
        cand_unique[row[2]] += 1
      else:
        cand_unique[row[2]]= 1
#writes header to txt file and prints to terminal, writes total vote count.
with open(exportpath,'w') as txt:
  header=(
    "Election Results\n"
    "-------------------\n"
    f"Total Votes: {vote_count} \n"
    "-------------------\n")
  print(header)
  txt.write(header)
  #new dictionary to take candidate names with percentage of wins, as well as an empty string to recieve winner name
  win_percent={}
  winner=''
  greatest_value=0
  #inside this for loop it calculates the candidates win percent using the cand_unique dictionary, and associated values
  #it also prints their percentage as it goes to the terminal and the txt file. Then it finds the winner by comparing 
  #number of votes for each candidate inside the cand_unique dictionary with the if statement
  for candidate in cand_unique:
    win_percent[candidate]=round(cand_unique.get(candidate)/vote_count*100,2)
    print(candidate +" "+ str(win_percent.get(candidate))+"%"+ " ("+ str(cand_unique.get(candidate))+")" )
    txt.write(candidate +" "+ str(win_percent.get(candidate))+"%"+ " ("+ str(cand_unique.get(candidate))+")\n" )
    if cand_unique.get(candidate) > greatest_value:
      winner=candidate 
      greatest_value=cand_unique.get(candidate)
  print("----------------\n"
    "The winner is :" + winner )
  txt.write("----------------\n"
    "The winner is :" + winner)




             

