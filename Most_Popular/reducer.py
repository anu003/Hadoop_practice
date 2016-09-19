import sys

oldKey = None
hits = 0
maxHits = 0
maxHitsKey = None

for line in sys.stdin:
    data_mapped = line.strip().split()

    if len(data_mapped) != 1:
        continue

    thisKey = data_mapped[0]

    if oldKey and oldKey != thisKey:
        if hits > maxHits:
            maxHits = hits
            maxHitsKey = oldKey
        hits = 0

    oldKey = thisKey
    hits += 1

print maxHitsKey, '\t', str(maxHits)
