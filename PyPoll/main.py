import os
import csv

electioncsv = os.path.join('..','Resources','election_data.csv')
exportpath= os.path.join('..','Resources','election_results.txt')

vote_count=0
cand_unique={}
with open(electioncsv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header=next(csvreader)
   # print(csv_header)
    
    for row in csvreader:
      vote_count += 1
      if row[2] in cand_unique.keys():
        cand_unique[row[2]] += 1
      else:
        cand_unique[row[2]]= 1

with open(exportpath,'w') as txt:
  header=(
    "Election Results\n"
    "-------------------\n"
    f"Total Votes: {vote_count} \n"
    "-------------------\n")
  print(header)
  txt.write(header)
  win_percent={}
  winner=''
  greatest_value=0
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




             

