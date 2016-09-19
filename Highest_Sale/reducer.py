import sys

maxSale = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split('\t')
    if len(data_mapped) != 2:
        #skip this line
        continue

    thisKey, thisSale = data_mapped
    thisSale = float(thisSale)

    if thisSale > maxSale:
        maxSale = thisSale

    if oldKey and oldKey != thisKey:
        print oldKey, '\t', maxSale
        maxSale = 0

    oldKey = thisKey
    salesTotal += float(thisSale)

if oldKey != None:
    print oldKey, '\t', maxSale
