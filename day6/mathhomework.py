from collections import defaultdict
from math import prod
# from pandas import DataFrame

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

    # I think all i really need to do is transpose it?
    with open('input') as f:
        stuff = [ list(i.rstrip('\n')) for i in f.readlines() ]
    tp_stuff = list(map(list,zip(*stuff)))
    back_to_string = ''
    for l in tp_stuff:
        back_to_string += (''.join(l)) + '\n'

    problems = back_to_string.split(' '*len(stuff))
    grand_total = 0
    for p in problems:
        numbers = p.strip().split('\n')
        operation = numbers[0][-1]
        numbers[0] = numbers[0][:-1]
        numbers = [ int(n) for n in numbers ]
        if operation == '+':
            grand_total += sum(numbers)
        else:
            grand_total += prod(numbers)

    print(grand_total)
        
        
