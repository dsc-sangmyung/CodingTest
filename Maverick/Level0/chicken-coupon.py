def solution(chicken):
    answer = 0
    while chicken >= 10:
        coupons = chicken // 10
        add = chicken % 10
        answer += coupons
        chicken = add + coupons
    return answer

cnt = int(input())
print(solution(cnt))
