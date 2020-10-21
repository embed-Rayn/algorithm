list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
print(list(map(lambda a, b: a * b, list1, list2)))

array = [('a', 50), ('b', 32), ('c', 74)]
print(sorted(array, key=lambda x: x[1], reverse=True))

result = sum([1, 2, 3, 4, 5])
print(result)

min_result = min(7, 3, 5, 2)
max_result = max(7, 3, 5, 2)
print(min_result, max_result)

result = eval("(3 + 5) * 7")
print(result)

from itertools import permutations
from itertools import combinations

data = ['A', 'B', 'C']

per_rst = list(permutations(data, 2))
print(per_rst)

com_rst = list(combinations(data, 2))
print(com_rst)

from collections import Counter
counter = Counter(['red', 'red', 'red', 'blue', 'blue', 'green'])
print(counter)

import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

a = 21
b = 14
print(math.gcd(21, 14))
print(lcm(21, 14))