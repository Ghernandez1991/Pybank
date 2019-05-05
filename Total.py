import csv

#this code produces the net amount of profit and losses over the csv file. 
with open('budget_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    total = 0
    for row in csv.reader(csv_file):
        total += int(row[1])
    print ("Total:", total)
 


