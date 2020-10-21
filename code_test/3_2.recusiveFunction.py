def recursive_function(i):
    if i == 3:
        return
    print("{} 번째 재귀함수에서 {} 번재 째귀 함수를 호출".format(i, i + 1))
    recursive_function(i + 1)
    print("{} 번째 재귀함수 종료".format(i))
recursive_function(1)

def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n - 1) * n
print(factorial(5))

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

print(gcd(192, 162))