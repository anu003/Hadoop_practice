import sys

fantascticTotal = 0
fantastically_list = []
for line in sys.stdin:
    data_mapped = line.strip().split('\t')

    if len(data_mapped) != 2:
        continue

    word, node_id = data_mapped
    if 'fantastic' in word:
        fantascticTotal += 1

    if 'fantastically' in word:
        fantastically_list.append(node_id)
        fantastically_list = sorted(fantastically_list)

print fantascticTotal, '\t', ' '.join(fantastically_list)
