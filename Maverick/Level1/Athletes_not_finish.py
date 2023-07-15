def solution(participant, completion):
    answer = ''

    participant.sort()
    completion.sort()

    for find in range(len(completion)):
        if(participant[find] != completion[find]):
            return participant[find]
    
    return participant[-1]
