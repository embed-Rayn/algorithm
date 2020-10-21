for i in range(5):
    for j in range(5):
        print("({}, {})".format(i, j), end ="\t")
    print()
#     R  U   L  D
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

x, y = 1, 1
#data = list(map(str, input().split()))
data = 'R R R U D'
print(data)
for val in data:
    if(val == 'R'):
        y += dy[0]
    elif (val == 'U'):
        x += dx[1]
    elif (val == 'L'):
        y += dy[2]
    elif (val == 'D'):
        x += dx[3]
    if x < 1:
        x = 1
    elif y < 1:
        y = 1

#N = int(input())
N = 5
time = [0, 0, 0]
cnt = 0
for i in range((N + 1) * 3600 - 1):
    time[2] += 1
    if time[2] == 60:
        time[1] += 1
        time[2] = 0
        if time[1] ==60:
            time[0] += 1
            time[1] = 0
    if time[0] % 10 == 3 or time[0] // 10 == 3 or time[1] % 10 == 3 or time[1] // 10 == 3 or time[2] % 10 == 3 or time[2] // 10 == 3:
        cnt +=1
print(cnt)

#data = input()
data = 'a1'
data = [val for val in data]
x = ord(data[0]) - 97
y = int(data[1]) - 1
possible_pos = []
for x_a in [2, -2]:
    for y_a in [1, -1]:
        possible_pos.append([x + x_a, y + y_a])
for x_a in [1, -1]:
    for y_a in [2, -2]:
        possible_pos.append([x + x_a, y + y_a])
cnt = 0
for pos in possible_pos:
    if pos[0] > 0 and pos[1] > 0 and pos[0] < 8 and pos[1] < 8:
        cnt += 1
print(cnt)

data = "K1KA5CB7"
data = "AJKDLSI412K4JSJ9D"
char_list = []
int_list = []
for char in data:
    if ord(char) > 64 and ord(char) < 93:
        char_list.append(char)
    else:
        int_list.append(int(char))
char_list.sort()
for char in char_list:
    print(char, end='')
print(sum(int_list))