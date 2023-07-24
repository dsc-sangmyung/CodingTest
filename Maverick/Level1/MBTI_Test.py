def solution(survey, choices):
    answer = ''
    mbti = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    for i in range(len(survey)):
        l = survey[i][0]
        r = survey[i][1]
        if choices[i]-4>0:
            mbti[r] += choices[i]-4
        elif choices[i] - 4 <0:
            mbti[l] += 4 - choices[i]
    answer += 'R' if mbti['R']>=mbti['T'] else 'T'
    answer += 'C' if mbti['C']>=mbti['F'] else 'F'
    answer += 'J' if mbti['J']>=mbti['M'] else 'M'
    answer += 'A' if mbti['A']>=mbti['N'] else 'N'

    return answer

survey = list(map(str,input().split()))
choices = list(map(int,input().split()))

print(survey)
print(choices)
print(solution(survey,choices))