def GCD(a,b):
    while b != 0:
        a, b = b, a % b
    return a
def solution(a, b):
    gcd = GCD(a, b)
    a //= gcd
    b //= gcd

    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5
    
    if b == 1:
        return 1
    else: 
        return 2

print(solution(7,20))
print(solution(11,22))
print(solution(12,21))
