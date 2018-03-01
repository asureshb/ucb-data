#!/usr/local/bin/python

#
#  PyBank/main.py is to analyze budget data of banks and display summary of analysis
#  Syntax: python PyBank/main.py <csv_file_path>
#

import csv
import sys

def AnalyzeBudgetData(file):

    fd = open(file, 'r')
    budget_data = csv.DictReader(fd)

    budget_dates = []
    budget_revenues = []
    for row in budget_data:
        budget_dates.append([row['Date']])
        budget_revenues.append(row['Revenue'])

    # total months
    total_months = len(budget_dates)

    # convert all the values in list from string to integer type
    budget_revenues = [int(x) for x in budget_revenues if x]

    revenueDiffList = []
    for i in range(0, total_months-1):
        revenueDiffList.append(budget_revenues[i] - budget_revenues[i+1])

    # calculate average revenue difference
    averageRevenueDiff = sum(revenueDiffList) / len(revenueDiffList)

    # calculate maximum revenue difference and date
    maxRevenueDiff = max(revenueDiffList)
    maxRevenueDiff_Index = revenueDiffList.index(maxRevenueDiff)
    maxRevenueDiff_Date = budget_dates[maxRevenueDiff_Index]

    # calculate minimum revenue difference and date
    minRevenueDiff = min(revenueDiffList)
    minRevenueDiff_Index = revenueDiffList.index(minRevenueDiff)
    minRevenueDiff_Date = budget_dates[minRevenueDiff_Index]

    print("Financial Analysis")
    print("---------------------------")
    print("Total Months: " + str(total_months))
    print("Total Revenue: " + '${:,.2f}'.format(sum(budget_revenues)))
    print("Average Revenue Change: " + '${:,.2f}'.format(averageRevenueDiff))
    print("Greatest Increase in Revenue: ", maxRevenueDiff_Date, '${:,.2f}'.format(maxRevenueDiff))
    print("Greatest Decrease in Revenue: ", minRevenueDiff_Date, '${:,.2f}'.format(minRevenueDiff))

if __name__ == '__main__':
    AnalyzeBudgetData(sys.argv[1])
