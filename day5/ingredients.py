if __name__ == '__main__':
    with open('input') as f:
        lines = f.readlines()

    ranges = []
    available = []
    parsing_ranges = True
    for l in lines:
        if l == '\n':
            parsing_ranges = False
            continue
        if parsing_ranges:
            low,high = map(int, l.split('-'))
            ranges.append((low,high))
        else:
            available.append(int(l))
    fresh_count = 0
    for a in available:
        for r in ranges:
            if r[0] <= a <= r[1]:
                fresh_count += 1
                break

    print(fresh_count)

    possible_fresh_count = 0
    for r in ranges:
        this_range = range(r[0],r[1])
        possible_fresh_count += len(this_range)

    print(possible_fresh_count)