import math

def solution(chicken):
    coupon = chicken
    answer = 0
    
    while coupon >= 10:
        order = math.floor(coupon/10)
        answer += order
        coupon += order
        coupon -= order * 10
    
    return answer
