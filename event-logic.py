import csv
import json

csvfilename = "testcsv.csv"
jsonfilename = csvfilename.split(',')[0] + '.json'
csvfile = open(csvfilename, 'r')
jsonfile = open(jsonfilename, 'w')
reader = csv.DictReader('testcsv.csv')

fieldnames = ('Title', 'Time', 'Day', 'Month', 'Year', 'Decription', 'Rsvp Link')

output = []

for each in reader:
  row = {}
  for field in fieldnames:
    row[field] = each[field]
output.append(row)

json.dump(output, jsonfile, indent=2, sort_keys=True)
