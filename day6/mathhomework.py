from collections import defaultdict
from math import prod

if __name__ == '__main__':
    with open('input') as f:
        lines = f.readlines()

    columns = defaultdict(list)
    for l in lines:
        fields = l.split()
        if fields[0].isnumeric():
            for i in range(len(fields)):
                columns[i].append(int(fields[i]))
        else:
            for i in range(len(fields)):
                columns[i].append(fields[i].strip())

    grand_total = 0
    for c in columns.values():
        operation = c.pop()
        if operation == '+':
            grand_total += sum(c)
        else:
            grand_total += prod(c)

    print(grand_total)
