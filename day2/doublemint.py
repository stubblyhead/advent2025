if __name__ == '__main__':
    with open('input') as f:
        ranges = f.readline().split(',')

    valid_count = 0
    for r in ranges:
        start,end = map(int, r.split('-'))
        for n in range(start,end+1):
            n_str = str(n)
            if len(n_str) % 2 == 1:  # numbers with an odd numer of digits can't be valid
                continue
            
            if n_str[:len(n_str)//2] == n_str[len(n_str)//2:]:
                valid_count += n

    print(valid_count)