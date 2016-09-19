import sys

oldKey = None
hits = 0

for line in sys.stdin:
    data_mapped = line.strip().split()

    if len(data_mapped) != 1:
        continue

    thisKey = data_mapped[0]

    if oldKey and oldKey != thiKey:
        print oldKey, '\t', str(hits)
        hits = 0

    oldKey = thisKey
    hits += 1

if oldKey != None:
    print oldKey, '\t', str(hits)
