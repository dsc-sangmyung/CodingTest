def solution(a, b):
    while (b % 2 == 0):
        b /= 2
    while (b % 5 == 0):
        b /= 5
    return 1 if a % b == 0 else 2
