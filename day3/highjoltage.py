def get_local_maxima(num):
    maxima = []
    for i in range(len(num)):
        if i == 0:
            left = '1'
        else:
            left = num[i-1]
        if i == len(num)-1:
            right = '1'
        else:
            right = num[i+1]
        if left <= num[i] and num[i] >= right:
            if right != num[i]:
                maxima.append(i)
    return maxima    
        

if __name__ == '__main__':
    with open('testcase') as f:
        lines = list(map(str.strip, f.readlines()))

    joltage = 0

    for bank in lines:
        found = False
        for num in range(99,10,-1):
            # if found:
            #     break
            if num % 10 == 0:
                continue
            num = str(num)
            if bank.count(num[0]):
                tens_loc = bank.index(num[0])
                if bank.count(num[1],tens_loc+1):
                    if bank.index(num[0]) < bank.index(num[1],tens_loc+1):
                        joltage += int(num)
                        break
    print(joltage)

    for bank in lines:
        print(get_local_maxima(bank))

        # while len(bank) > 12:
        #     maxima = get_local_maxima(bank)
        #     left, right = 0, len(bank)
        #     if maxima[0] > 0:
        #         right = maxima[0]
        #     elif len(maxima) > 1:

        #     for i in range(10):
                