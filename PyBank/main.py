import os
import csv

#print("Hello Andrew")
#print(os.getcwd())
#os.chdir('Desktop/Python-challenge/Pybank')
#print(os.getcwd())

budget_csv = os.path.join('..','Resources','budget_data.csv')
exportpath= os.path.join('..','Resources','financial_analysis.txt')
months=[]
profits=[]
row=0
previous_month=0
net_change=[]
with open(budget_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
   # print(f'Header: {csv_header}')
    
    for row in csvreader:
        months.append(row[0])
        profits.append(int(row[1]))
        if previous_month != 0: 
            net_change.append(int(row[1])-previous_month) 
        previous_month=int(row[1])

month_total=len(months)
net_profit=sum(profits)

#print('Total months= '+ str(month_total)+ ' and total profit= $' + str(net_profit))

average_change=round(sum(net_change)/month_total,2)
#print('Average change= $'+str(average_change))

greatest_increase=profits[0]
greatest_decrease=profits[0]


for i in range(len(net_change)):
    if net_change[i] >= greatest_increase:
        greatest_increase=net_change[i]
        greatest_month=months[i+1]
    elif net_change[i]<= greatest_decrease:
        greatest_decrease=net_change[i]
        decrease_month=months[i+1]
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

with open(exportpath, 'w') as txt:
    txt.write(output)














