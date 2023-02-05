while True:
    try:
        s = input()
        odd = sum([int(s[i]) for i in range(0, len(s), 2)])
        even = sum([int(s[i]) for i in range(1, len(s), 2)])
    except:
        break
    if s == "0":
        break
    if (odd-even)%11:
        print(s, 'is not a multiple of 11.')
    else:
        print(s, 'is a multiple of 11.')