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
            # if i == 0 and num[0] == num[1]:
            #     maxima.append(i)
            if right != num[i]:
                maxima.append(i)
    return maxima    
        

if __name__ == '__main__':
    with open('input') as f:
        lines = list(map(str.strip, f.readlines()))

    joltage = 0

    for bank in lines:
        found = False
        for num in range(99,10,-1):
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

    joltage = 0
    for bank in lines:
        for i in range(1,10):
            while bank.count(str(i)):
                if len(bank) == 12:
                    break
                low_num = bank.index(str(i))
                bank = bank[0:low_num] + bank[low_num+1:len(bank)]
                
        print(bank)
        joltage += int(bank)

    print(joltage)