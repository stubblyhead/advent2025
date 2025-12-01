with open('input') as f:
    turns = f.readlines()

zero_stop = 0
current_pos = 50

for t in turns:
    dist = int(t[1:])
    if t[0] == 'L':
        current_pos = (current_pos - dist) % 100
    else:
        current_pos = (current_pos + dist) % 100

    if current_pos == 0:
        zero_stop += 1

print(zero_stop)

current_pos = 50
zero_pass = 0

for t in turns:
    dist = int(t[1:])
    full_turns = dist // 100
    zero_pass += full_turns
    dist = dist % 100
    if current_pos == 0:
        continue
    if t[0] == 'L':
        current_pos -= dist
        if current_pos < 0:
            zero_pass += 1
            current_pos %= 100
    else:
        current_pos += dist
        if current_pos > 99:
            zero_pass += 1
            current_pos %= 100
    
print(zero_pass)