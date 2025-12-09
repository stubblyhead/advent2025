def numify(s):
    a,b = s.split(',')
    return((int(a),int(b),))

if __name__ == '__main__':
    with open('testcase') as f:
        lines = map(str.strip, f.readlines())

    reds = [ numify(l) for l in lines ]

    print(reds)    