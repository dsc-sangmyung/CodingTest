# 신고 결과 받기
# 코드가 너무 비효율적인데...

def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    report_result = [0 for _ in range(len(id_list))]
    block_user = []
    report = list(set(report))      # set 자료형으로 중복 제거

    for i in range(len(report)):
        temp = list(map(str, report[i].split()))
        id_index = id_list.index(temp[1])
        report_result[id_index] += 1

    for i in range(len(report_result)):
        if report_result[i] >= k:
            block_user.append(id_list[i])
        else:
            continue

    for i in range(len(report)):
        temp = list(map(str, report[i].split()))
        id_index = id_list.index(temp[0])
        if temp[1] in block_user:
            answer[id_index] += 1
        else:
            continue

    return answer

solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)
solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)
