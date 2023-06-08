def solution(n):
    answer = 0
    for _ in range(0, n):
        answer += 1
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1
    return answer
