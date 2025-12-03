if __name__ == '__main__':
    with open('input') as f:
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
                if bank.count(num[1],tens_loc):
                    if bank.index(num[0]) < bank.index(num[1],tens_loc):
                        joltage += int(num)
                        print(bank, num)
                        break

    
    print(joltage)