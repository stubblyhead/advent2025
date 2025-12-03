def get_local_maxima(num):
        maxima = []
        for i in range(len(num)):
            if i == 0:
                left = '0'
            else:
                left = num[i-1]
            if i == len(num)-1:
                right = '0'
            else:
                right = num[i+1]
            if left < num[i] and num[i] > right:
                maxima.append(i)
        return maxima

if __name__ == '__main__':
    with open('testcase') as f:
        lines = f.readlines()

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
        while len(bank) > 12:
            maxima = get_local_maxima(bank)