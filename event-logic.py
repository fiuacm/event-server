import csv
import json

csvfilename = "testcsv.csv"
jsonfilename = csvfilename.split(',')[0] + '.json'
csvfile = open(csvfilename, 'r')
jsonfile = open(jsonfilename, 'w')
reader = csv.DictReader(testcsv)

fieldnames = (Title, Time, Day, Month, Year, Decription, Rsvp Link)
