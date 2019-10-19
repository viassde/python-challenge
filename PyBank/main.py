import os
import csv

budget_csv_path = os.path.join("Resources", "budget_data.csv")
with open(budget_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    next(csv_reader) # skip header row

    tot_mo =0       #month counter
    net_pnl =0      #net P&L
    change =0       #initialize change
    max_change =0   #initialize max increase
    min_change =0   #initialize max decrease
    prev =0         #auxiliary variable to compute P&L changes
    add_change =0   #initialize add changes 

    # Read through each row of data after the header
    for row in csv_reader:

        tot_mo = tot_mo + 1
    
        net_pnl = net_pnl + float(row[1]) #add P&L
        if (tot_mo ==1):    #change =0 for first month (by definition)
            change =0
        else:
            change =float(row[1]) - prev  #compute change
        
        add_change =add_change + change   #add changes

        prev =float(row[1])
        if change > max_change:     #max increase
            max_change = change
            max_chdate =(row[0])
        if change < min_change:     #min decrease
            min_change = change
            min_chdate =(row[0])

    ave_change =add_change/(tot_mo-1)  #average change
    ave_change =round(ave_change,2)

msg = f' Total Months: {tot_mo} Total: ${int(net_pnl)} Average Change: ${ave_change} Greatest Increase in Profits: {max_chdate} (${int(max_change)}) Greatest Decrease in Profits: {min_chdate} (${int(min_change)}) ``` '

# results to terminal
print(' ```text Financial Analysis ' )
print(msg)

# results to text file 
f = open("results.txt", "w")
f.write(msg)
f.close()

