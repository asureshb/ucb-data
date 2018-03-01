#!/usr/local/bin/python

#
#  PyBoss/main.py is to format employee records
#  Syntax: python PyBoss/main.py <csv_file_path> <output_file_path>
#

#import all required modules here
import csv
import sys

def FormatEmployeeRecords(employeeData_csv, employeeData_newFormat_csv):
    us_state_codes = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY'
    }

    # open file and read employee data
    fd = open(employeeData_csv, 'r')
    employeeData = csv.DictReader(fd)

    # create a csv writer object to write reformatted employee data
    fdw = open(employeeData_newFormat_csv, 'w')
    csvWriter = csv.DictWriter(fdw, fieldnames=["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])
    csvWriter.writeheader()
    
    for row in employeeData:

        # split date into year, month, date to reformat
        (y, m, d) = row['DOB'].split("-")

        csvWriter.writerows([{
                                'Emp ID': row['Emp ID'],
                                'First Name': row['Name'].split(" ")[0],
                                'Last Name': row['Name'].split(" ")[1],
                                'DOB': "%s/%s/%s" % (d, m, y),
                                'SSN': "***-**-%s" % row['SSN'].split("-")[2],
                                'State': us_state_codes[row['State']]
                           }])
 
if __name__ == '__main__':
    FormatEmployeeRecords(sys.argv[1], sys.argv[2])
