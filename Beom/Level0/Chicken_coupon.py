def solution(chicken): 
    coupon = chicken 
    answer = 0 
    while coupon >= 10:
        service = coupon//10
        answer += service
        coupon = coupon % 10 + service     

    return answer


print(solution(100))
print(solution(1081))

