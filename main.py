#dependencies
import csv
#list to collect the changes in profts
arrPlChg = []
#variables to be called later
rowcnt = 1
maxchg = 0
minchg = 0
#open csv
with open('budget_data.csv', 'r') as csv_file:
    #pass through csv reader
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    
    firstime = True
    firstchg = True
#start looping through column
    for row in csv_reader:
        if firstime:
            pre_pl = float(row[1])
            arrPlChg.append(0)
            firstime = False
            rowcnt += 1
            next
        else:
            cur_pl = float(row[1]) 
            varpl =  float(cur_pl) - float(pre_pl)
            arrPlChg.append(varpl)
            if firstchg:
                minchg = varpl
                maxchg = varpl
                minDate = row[0]
                maxDate = row[0]
                firstchg = False
            elif minchg <  varpl:
                minDate = row[0]
                minchg = varpl
            elif varpl >  maxchg:
                    maxDate = row[0]
                    maxchg = varpl

        pre_pl = row[1]
    #sum of list
    sumArr = sum(arrPlChg)
    #lenght of list
    arrcnt = len(arrPlChg) -1
    #average=sum/length
    varmean= sumArr/arrcnt 
    
    print("Average  Change: ", varmean)
#max of the list
    Max_change = max(arrPlChg)
    #min of the list
    Min_change = min(arrPlChg)
    print("Greatest Increase in Profits: ", maxDate, "  ", Max_change)
    print("Greatest Decrease in Profits: ", minDate, "  ", Min_change)
    #putting this here because when I put it at the top it gives max()arg is empty
    # standlone this code returns the total months 
    
with open('budget_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    value = len(list(csv_reader))
    print("Total Months", value)
