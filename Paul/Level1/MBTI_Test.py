def solution(survey, choices):

    score_list = [3, 2, 1, 0, 1, 2, 3]
    result = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}

    for i in range(len(survey)):

        temp = list(survey[i])              # 유형 나누기
        score_index = choices[i] - 1        # 점수 인덱스
        
        if score_index > 3:
            result[temp[1]] += score_list[score_index]
        elif score_index < 3:
            result[temp[0]] += score_list[score_index]
        else:
            continue

    answer = ''

    if result["R"] >= result["T"]:
        answer += "R"
    else:
        answer += "T"

    if result["C"] >= result["F"]:
        answer += "C"
    else:
        answer += "F"

    if result["J"] >= result["M"]:
        answer += "J"
    else:
        answer += "M"

    if result["A"] >= result["N"]:
        answer += "A"
    else:
        answer += "N"

    return answer
