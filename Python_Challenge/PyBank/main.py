#
#  PyBank/main.py is to analyze budget data of banks and display summary of analysis
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
    for i in range(len(budget_revenues) -1):
        revenueDiffList.append(budget_revenues[i] - budget_revenues[i+1])

    averageRevenueDiff = sum(revenueDiffList) / len(revenueDiffList)
    print("Average Revenue Diff: " + str(averageRevenueDiff))

    #print("Financial Analysis")
    #print("---------------------------")
    print("Total Months: " + str(total_months))
    print("Total Revenue: " + '${:,.2f}'.format(sum(budget_revenues)))

if __name__ == '__main__':
    AnalyzeBudgetData(sys.argv[1])
