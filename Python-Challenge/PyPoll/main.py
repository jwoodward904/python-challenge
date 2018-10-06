import os 
import csv

canidates=["Khan","Correy","Li","O'Tooley"]
Khan=0
Correy=0
Li=0
OTooley=0
Winner=str("")
with open("election_data.csv",newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    csv_header=next(csvreader)
    row_count = sum(1 for row in csv.reader( open('election_data.csv') ) )
 
    for row in csvreader:
          for row in csvreader:
            if str(row[2]) == canidates[0]:
                Khan=Khan+1
            if str(row[2]) == canidates[1]:
                Correy=Correy+1
            if str(row[2]) == canidates[2]:
                Li=Li+1
            if str(row[2]) == canidates[3]:
                OTooley=OTooley+1 
            Results=[str(OTooley),str(Li),str(Correy),str(Khan)]
            Results.sort(reverse=True)
            if Results[0] == OTooley:
                    Winner="O'Tooley"
            elif Results[0] == Li:
                     Winner="Li"
            elif Results[0] == Correy:
                     Winner="Correy"
            else:
                     Winner="Khan"


a=format(round(float(((Khan+1)/row_count)*100.000),3), '.3f')
b=format(round(float(((Correy+1)/row_count)*100.000),3), '.3f')
c=format(round(float(((Li+1)/row_count)*100.000),3), '.3f')
d=format(round(float(((OTooley+1)/row_count)*100.000),3), '.3f')


print("Election Results")
print("-------------------------")
print("Total Votes: " + str(row_count-1))
print("-------------------------")          
print(canidates[0]+": "+ str(a) +"% (" +str(Khan+1)+")")
print(canidates[1]+": "+ str(b) +"% (" +str(Correy)+")") 
print(canidates[2]+": "+ str(c) +"% (" +str(Li)+")") 
print(canidates[3]+": "+ str(d) +"% (" +str(OTooley)+")")              
print("-------------------------")
print("Winner:" + Winner)
print("-------------------------")

myData=[["Election Results"],
["-------------------------"],
["Total Votes: " + str(row_count-1)],
["-------------------------"],
[canidates[0]+": "+ str(a) +"% (" +str(Khan+1)+")"],
[canidates[1]+": "+ str(b) +"% (" +str(Correy)+")"],
[canidates[2]+": "+ str(c) +"% (" +str(Li)+")"],
[canidates[3]+": "+ str(d) +"% (" +str(OTooley)+")"],
["-------------------------"],
["Winner:" + Winner],
["-------------------------"]]

myFile = open('Poll Results.csv', 'w',newline='')  
with myFile:
   writer = csv.writer(myFile)
   writer.writerows(myData)

