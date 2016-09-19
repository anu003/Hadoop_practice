import sys

numberSales = 0
salesTotal = 0

for line in sys.stdin:
    data_mapped = line.strip().split('\t')

    if len(data_mapped) != 2:
        continue

    _, thisSales = data_mapped
    salesTotal += float(thisSales)
    numberSales += 1

print numberSales, salesTotal
