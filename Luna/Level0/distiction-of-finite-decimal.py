# 유한소수 판별하기

import math

def solution(a, b):
    tmp = b//math.gcd(a,b)

    while tmp%2 == 0 :
        tmp //= 2
    while tmp%5 == 0 :
        tmp //= 5
    
    return 1 if tmp == 1 else 2
