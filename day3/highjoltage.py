def get_split(numstr, length):
    strlen = len(numstr)
    left = numstr[:strlen-length]
    right = numstr[strlen-length:]
    return(left,right)
        

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

    # select 12 numbers from 15 numbers--the first number must be no later than the
    # 4th number, or else there won't be enough numbers left.  
    #  1           2-12
    # xxxx  |  xxxxxxxxxxx
    # so keep (numbers needed - 1) in reserve, and keep the left most highest digit 
    # from the front part.  discard all numbers before that number, and append the
    # rest of the left side with the right side.  Repeat.  

    for bank in lines:
        found_biggest = False
        biggest_battery = ''
        for i in range(11,0,-1):
            if found_biggest:
                break
            left,right = get_split(bank, i)
            # if left == '':
            #     biggest_battery += right
            #     found_biggest = True
            #     break
            for i in range(9,0,-1):
                if left.count(str(i)):
                    biggest_battery += str(i)
                    break
            
            bank = left[left.index(str(i))+1:] + right
        print(biggest_battery)
        
        joltage += int(biggest_battery)

    print(joltage)
        
