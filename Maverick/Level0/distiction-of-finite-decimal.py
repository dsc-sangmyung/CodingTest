import math
def solution(a, b):
    gcd_value = math.gcd(a, b)
    b = b // gcd_value
    while b % 2 == 0:
        b = b // 2
    while b % 5 == 0:
        b = b // 5
    if b == 1:
        return 1
    else:
        return 2

a,b = map(int,input().split())
print(solution(a,b))