for _ in range(int(input())):
    n, *arr = map(int, input().split())
    arr.sort()
    mid = n//2
    cnt = 0
    for i in arr:
        cnt += abs(arr[mid]-i)
    print(cnt)