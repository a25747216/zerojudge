while True:
    try:
        x, y = map(int, input().split())
    except:
        break
    print(abs(x - y))