# 크기가 작은 부분문자

def solution(t, p):
    result = []

    list_t = list(map(int, str(t)))
    list_p = list(map(int, str(p)))
    length_p = len(list_p)

    for i in range(len(list_t) - length_p + 1):
        temp_list = []
        temp_list.append(list_t[i:i + length_p])
        temp = 0
        count = length_p
        for j in range(length_p):
            count -= 1
            temp = temp + (temp_list[0][j] * 10 ** count)

        temp = int(temp)

        if temp <= p:
            result.append(temp)

    print(len(result))

solution(3141592, 271)
solution(500220839878, 7)
solution(10203, 15)
