import csv
from parse_tse import last_price

with open('portfolio.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    portfolio = {}
    lp = {}
    values = {}
    total_value = 0
    for row in reader:
        lp.update({row[0]: last_price(row[0])})
        portfolio.update({row[0]: int(row[1])})
        values.update({row[0]: portfolio[row[0]]*lp[row[0]]})
        total_value += values[row[0]]
print('{0:12s} {1:10s} {2:8s} {3:8s} {4:4}'.format('نماد', 'تعداد', 'قیمت', 'ارزش', 'درصد'))
print('-------------------------------------------------')
for value in sorted(values.values(), reverse=True):
    key = [k for k, v in values.items() if v == value][0]
    print("{0:12s} {1:8} {2:8} {3:8} {4:8.1f}".format(key, portfolio[key], lp[key], int(values[key]/10000000), values[key]/total_value*100))

print('\nارزش سبد سهام: ', int(total_value/10000000))
print('\nارزش سبد دارایی: ', int(total_value/10000000)+217)