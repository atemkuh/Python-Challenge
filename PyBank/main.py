import os
import csv
import operator
from collections import defaultdict

#Create your 3 dictionaries to store data
budget_dict = {}
increase_dict = {}
decrease_dict = {}

#Open the csv file (specify the path to csv file below
with open("/Users/atemkuh/Documents/GitHub/Python-Challenge/Pybank/Resources/budget_data.csv") as csvfile:
#with open("Resources","budget_data.csv") as csvfile:

    #Read the csv file
    readCSV = csv.reader(csvfile, delimiter=',')

    #Create dates and profits arrays
    dates = []
    profits = []

    #loop the csv file to read its data
    for row in readCSV:
        date = row[0]
        profit = row[1]

    #Store dates and profits into their respective arrays
        dates.append(date)
        profits.append(profit)

#Populate the dictionary with date keys and profit values
    for t in range (1, len(dates)):
        budget_dict[dates[t]] =(int(profits[t]))

    for t in range (1, len(dates)):
        if int(profits[t]) > 0:
            increase_dict[dates[t]] =(int(profits[t]))

    for t in range (1, len(dates)):
        if int(profits[t]) < 0:
            decrease_dict[dates[t]] =(int(profits[t]))

#Generate your report
    greatest_increase = max(budget_dict, key=budget_dict.get)
    greatest_derease = min(decrease_dict, key=decrease_dict.get)
    total_value = sum(budget_dict.values())
    total_months = len(dates)-1

#Display your report to the terminal
    print("Financial Analysis \n------------------------\nTotal Months: %s" %(total_months))
    print("Total: $" +str(total_value))
    print("Greatest Increase in Profits: %s ($%s)" %(greatest_increase, increase_dict[greatest_increase]))
    print("Greatest Decrease in Profits: %s ($%s)" %(greatest_derease, decrease_dict[greatest_derease]))

#Generate your Report.txt file (replace the path directory)
    with open("/Users/atemkuh/Documents/GitHub/Python-Challenge/Pybank/Report.txt", "a") as file:
        file.write("Financial Analysis\n")
        file.write("-------------------\n")
        file.write("\nTotal Months: %s" %(total_months))
        file.write("\nTotal: $" +str(total_value))
        file.write("\nGreatest Increase in Profits: %s ($%s)" %(greatest_increase, increase_dict[greatest_increase]))
        file.write("\nGreatest Decrease in Profits: %s ($%s)" %(greatest_derease, decrease_dict[greatest_derease]))

        file.close()

# --------------------------- END ------------------------
