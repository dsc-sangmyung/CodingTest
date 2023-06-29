def solution(t, p):
    answer = 0
    p_len = len(p)
    p = int(p)
    for i in range(len(t)-p_len+1):
        if int(t[i:i+p_len]) <= p:
            answer += 1
    return answer


a,b = input().split()

print(solution(a,b))
