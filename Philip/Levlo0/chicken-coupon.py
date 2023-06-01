def solution(chicken):
    answer = 0
    spare = 0
    while chicken>=10 :
        spare = chicken % 10
        chicken = int(chicken / 10)
        answer += chicken
        chicken += spare
    return answer
