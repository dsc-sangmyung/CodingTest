def solution(chicken): 
    coupon = chicken 
    answer = 0 
    while coupon >= 10:
        service = coupon//10
        coupon = coupon % 10 + service
        answer += service    
    return answer


print(solution(100))
print(solution(1081))

