import sys,re

i = 0
for line in sys.stdin:
    #to skip the column names
    if i:
        data = line.strip().split('\t')
        if len(data) == 19:
            node = data[0]
            review = data[4].lower()
            words = ' '.join(re.findall(r'[a-z]+', review.strip())).split()
            for word in words:
                print word, '\t', node
    i += 1
