ans = {}
for _ in range(int(input())):
    try:
        country = input().split()[0]
    except:
        break
    if country in ans:
        ans[country]+=1
    else:
        ans[country]=1
    
ans =  {k:v for k,v in sorted(ans.items())}

for k, v in ans.items():
    print(k, v)