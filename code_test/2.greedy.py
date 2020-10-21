#data = input()
data = '02421'
data = [int(i) for i in data]
tot = data[0]
for i in range(len(data) - 1):
    if data[i + 1] <= 1 or tot <= 1:
        tot += data[i + 1]
    else:
        tot *= data[i + 1]
print(tot)
import numpy as np
for _ in range(10):
    N = 5#input()
    data = '2 3 1 2 2'#input()
    data = [np.random.randint(1, 5) for _ in range(10)]
    #data = list(map(int, data.split()))

    result = 0
    count = 0
    for i in data:
        count += 1
        if count >= i:
            result += 1
            count = 0
    print("db ans", result)
