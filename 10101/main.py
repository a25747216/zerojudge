def f(n):
    if n>=10000000:
        f(n//10000000)
        print(" kuti",end ="")
        n%=10000000
    if n>=100000:
        f(n//100000)
        print(" lakh", end ="")
        n%=100000
    if n>=1000:
        f(n//1000)
        print(" hajar",end="")
        n%=1000
    if n >=100:
        f(n//100)
        print(" shata",end="")
        n%=100
    if n:
        print(f" {n}", end="")

case=1
while True:
    try:
        n = int(input())
    except:
        break
    print(f"{case}.", end="")
    if n:
        f(n)
    else:
        print(" 0",end="")
    print("")
    case+=1