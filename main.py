import csv
from parse_tse import last_price

with open('namad_test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    namads = {}
    for row in reader:
        namads.update({row[0]: last_price(row[0])})

print(namads)