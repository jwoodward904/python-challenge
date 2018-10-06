import os 
import csv
numlines = 0
total=0
avgchange=[]
month=[]
p_year=0
avg=0.00

with open("Budget_Data.csv",newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    csv_header=next(csvreader)    
    for row in csvreader:
        total+= int(row[1])
        numlines +=1
        c_year=int(row[1]) - p_year
        p_year=int(row[1])      
        avgchange.append(int(c_year))
        month.append(str(row[0]))
    del avgchange[0]   
avg=float(sum(avgchange)/len(avgchange))
max(avgchange)
min(avgchange)
increase=avgchange.index(max(avgchange))
decrease=avgchange.index(min(avgchange))

Tmonths="Total Months: " + str(numlines)
TDollars="Total: $" + str(total)
Tavgchange="Average  Change: $"+ str(round(float(avg),2))
PIncrease="Greatest Increase in Profits: " + month[increase]+ "($"+ str(avgchange[increase])+ ")"
PDecrease="Greatest Decrease in Profits: " + month[decrease]+ "($"+ str(avgchange[decrease])+ ")"

MyData=[[Tmonths],[TDollars],[Tavgchange],[PIncrease],[PDecrease]]

myFile = open('Budget Results.csv', 'w',newline='')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(MyData)
print("Total Months: " + str(numlines))
print("Total: $" + str(total))
print("Average  Change: $"+ str(round(float(avg),2)))
print("Greatest Increase in Profits: " + month[increase]+ "($"+ str(avgchange[increase])+ ")")
print("Greatest Decrease in Profits: " + month[decrease]+ "($"+ str(avgchange[decrease])+ ")")


