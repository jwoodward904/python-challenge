import os
import csv
#field names
fields = ['Name','Branch','Year']
# data rows of CSV file
rows = [['Stef', 'Multimedia Technology','2'],
    ['Kani', 'Information Technology', '2'],
    ['Plazaa', 'Electronics Engineering', '4'],
     ['Lizzy', 'Computer Science', '4'],
     ['Reshmi', 'Multimedia Technology', '3'],
     ['Geetha','Electrical Engineering', '4'],
     ['Keerti', 'Aeronautical Engineering', '3']]



with open('records.csv','w', newline='') as csvfile:
    #creating  a csv writer object
    csvwriter = csv.writer(csvfile)
    #writing the fields
    #csvwriter.writerow(fields)
    # writing the data rows
    csvwriter.writerows(rows)