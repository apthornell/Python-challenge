import os
import csv


#set import and export paths for files
budget_csv = os.path.join('..','Resources','budget_data.csv')
exportpath= os.path.join('..','Resources','financial_analysis.txt')
#declare variables and empty lists, and set row and previous month values to 0
months=[]
profits=[]
row=0
previous_month=0
net_change=[]

#opens file and moves past the header
with open(budget_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
   
 #appends month list for every month it moves through, then appends the net_change list with the 
 #difference between months taking into account the first iteration being 0 since there is not a previous
 #month to look to. Also loads the profits as integars so that they can be used to calculate later.  
    for row in csvreader:
        months.append(row[0])
        profits.append(int(row[1]))
        if previous_month != 0: 
            net_change.append(int(row[1])-previous_month) 
        previous_month=int(row[1])
#sets variables for the total months and gets calculation from the length of the months list
#gets net profit by summing all values in profits list
month_total=len(months)
net_profit=sum(profits)

#calculates the average change by summing the net change values, then dividing by total months. Rounded to two 
#decimal places so that it would look nicer
average_change=round(sum(net_change)/month_total,2)

greatest_increase=profits[0]
greatest_decrease=profits[0]

#loops through and finds the greatest increase by comparing values of net change, then corrects the offset 
#of the month since the loop is one behind the month it is looking at
for i in range(len(net_change)):
    if net_change[i] >= greatest_increase:
        greatest_increase=net_change[i]
        greatest_month=months[i+1]
    elif net_change[i]<= greatest_decrease:
        greatest_decrease=net_change[i]
        decrease_month=months[i+1]
#set print statements and print to terminal
output=(
    'Financial Analysis\n'
    '-----------------------------------\n'
    f'Total months: {month_total}\n'
    f'Total: $ {net_profit}\n'
    f'Average Change: ${average_change}\n'
    f'Greatest increase in profit =$ {greatest_increase}  in  {greatest_month}\n'
    'Greatest decrease in profit =$'+ str(greatest_decrease)+ ' in '+ str(decrease_month)+'\n'
    'Total Profit= $'+ str(net_profit))
print(output)
#wrote print statements to txt file ouput path as well so that it wouldn't be needed to be typed twice
with open(exportpath, 'w') as txt:
    txt.write(output)














