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

    ranges = sorted(ranges)
    
    consolidated_ranges = []

    while ranges:
        this_range = ranges.pop(0)
        if not ranges:
            consolidated_ranges.append(this_range)
            break
        if this_range[1] + 1 >= ranges[0][0]:
            ranges[0] = (this_range[0],max(ranges[0][1],this_range[1]))
        else:
            consolidated_ranges.append(this_range)
            
    possible_fresh = 0
    for c in consolidated_ranges:
        possible_fresh += len(range(c[0],c[1]+1))

    print(possible_fresh)

        
