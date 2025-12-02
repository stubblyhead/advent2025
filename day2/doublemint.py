import re

if __name__ == '__main__':
    with open('input') as f:
        ranges = f.readline().split(',')

    valid_count = 0
    valid_count_part2 = 0
    pattern = re.compile(r'^(\d+)\1+$')
    for r in ranges:
        start,end = map(int, r.split('-'))
        for n in range(start,end+1):
            n_str = str(n)
            if re.search(pattern, n_str):
                valid_count_part2 += n
            if len(n_str) % 2 == 0:  
                if n_str[:len(n_str)//2] == n_str[len(n_str)//2:]:
                    valid_count += n

    print(valid_count)
    print(valid_count_part2)

