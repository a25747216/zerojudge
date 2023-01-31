border_x, border_y = map(int, input().split())
dirs = {'N':0, 'E':1, 'S':2, 'W':3, 0:'N', 1:'E', 2:'S', 3:'W'}
arr = []
dx = (0, 1, 0, -1) # N E S W
dy = (1, 0, -1, 0)
while True:
    try:
        x, y, dir = input().split()
        x, y, dir = int(x), int(y), dirs[dir]
        instructions = list(input())
    except:
        break
    lost = False
    
    for i in instructions:
        if i == 'R':
            dir = (dir+1)%4
        elif i == 'L':
            dir = (dir-1+4)%4
        elif i == 'F':
            nx = x+dx[dir]
            ny = y+dy[dir]
            if nx >= 0 and nx <= border_x and ny >= 0 and ny <= border_y:
                x = nx
                y = ny
            elif (x, y) in arr:
                continue
            else:
                print(x, y, dirs[dir], "LOST")
                arr.append((x, y))
                lost = True
                break
    if not lost:
        print(x, y, dirs[dir])