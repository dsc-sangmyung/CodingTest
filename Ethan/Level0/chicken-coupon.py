def solution(chicken):
    total = 0
    while chicken >= 0.01:
        service = chicken / 10
        total += service
        chicken /= 10
    return int(total)
