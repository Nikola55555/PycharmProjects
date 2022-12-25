games = [input().split(';') for i in range(int(input()))]
d = {}
for game in games:
    if game[0] not in d:
        d[game[0]] = [0, 0, 0, 0, 0]
    if game[2] not in d:
        d[game[2]] = [0, 0, 0, 0, 0]
    if int(game[1]) > int(game[3]):
        d[game[0]][0] += 1
        d[game[2]][0] += 1
        d[game[0]][1] += 1
        d[game[2]][3] += 1
        d[game[0]][4] += 3
    elif int(game[1]) == int(game[3]):
        d[game[0]][0] += 1
        d[game[2]][0] += 1
        d[game[0]][2] += 1
        d[game[2]][2] += 1
        d[game[0]][4] += 1
        d[game[2]][4] += 1
    elif int(game[1]) < int(game[3]):
        d[game[0]][0] += 1
        d[game[2]][0] += 1
        d[game[0]][3] += 1
        d[game[2]][1] += 1
        d[game[2]][4] += 3
for k, v in d.items():
    print(f'{k}:{v[0]} {v[1]} {v[2]} {v[3]} {v[4]}')
