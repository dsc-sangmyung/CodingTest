# 유한소수 판별하기

def solution(a, b):
    answer = 0
    i_a = i_b = 2
    list_a = []
    list_b = []

    if b == 1:
        answer = 1

    while a != 1:
        if a % i_a == 0:
            list_a.append(i_a)
            a = a // i_a
        else:
            if i_a > a:
                break
            i_a = i_a + 1

    while b != 1:
        if b % i_b == 0:
            list_b.append(i_b)
            b = b // i_b
        else:
            if i_b > b:
                break
            i_b = i_b + 1

    for index_a in range(len(list_a)):
        for index_b in range(len(list_b)):
            if list_a[index_a] == list_b[index_b]:
                list_b.pop(index_b)
                list_b.append(1)
                break

    for i in list_b:
        if i == 2 or i == 5 or i == 1:
            answer = 1
        else:
            answer = 2
            break
    
    return answer
