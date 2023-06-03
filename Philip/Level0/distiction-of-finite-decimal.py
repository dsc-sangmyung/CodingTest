def solution(a, b):
    answer = 1
    i = 2
    while (i <= a and i <= b) :
        if(a % i == 0 and b % i == 0) :
            a = a / i
            b = b / i
        else :
            i = i + 1
    j = 2
    while(b >= j) :
        if (b % j == 0):
            if(j == 2 or j == 5):
                b = b / j
            else :
                answer = 2
                break
        else:
            j = j + 1
    return answer
