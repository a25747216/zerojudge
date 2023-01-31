flag = 0
while True:
    try:
        s = list(input())
    except:
        break
    for idx, c in enumerate(s):
        if c == '"':
            if not flag:
                s[idx] = '``'
                flag = 1
            else:
                s[idx] = "''"
                flag = 0
    print("".join(s))