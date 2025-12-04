def get_split(numstr, length):
    strlen = len(numstr)
    left = numstr[:strlen-length+1]
    right = numstr[strlen-length+1:]
    return(left,right)
        

if __name__ == '__main__':
    with open('testcase') as f:
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
        found_biggest = False
        biggest_battery = ''
        for i in range(11,0,-1):
            if found_biggest:
                break
            left,right = get_split(bank, i)
            for i in range(9,0,-1):
                if left.count(str(i)):
                    biggest_battery += str(i)
                    break
            bank = left[left.index(str(i))+1:] + right
            if len(biggest_battery) + len(bank) == 12:
                biggest_battery += bank
                found_biggest = True
        print(biggest_battery)
        
        joltage += int(biggest_battery)

    print(joltage)
        
