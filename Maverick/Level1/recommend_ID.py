
def solution(new_id):

    answer = ''
    #1step
    new_id = new_id.lower()  
    #2step
    for i in new_id:
        if i.isalnum() or i in '-_.':
            answer += i
    #3step
    for i in new_id:
        if i in '..':
            answer = answer.replace('..','.')
    #4step
    if answer.startswith('.'):
        answer = answer[1:]
    if answer.endswith('.'):
        answer = answer[:-1]

    #5step
    if answer == "":
        answer = 'a'

    #6step
    if len(answer) > 15:
        answer = answer[:15]
        if answer.endswith('.'):
            answer = answer[:-1]

    #7step
    if len(answer)<3:
        answer += answer[-1] * (3-len(answer))

    return answer


a = input()
print(solution(a))