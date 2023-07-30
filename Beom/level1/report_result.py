def solution(id_list, report, k):
    answer = []
    report_people = []      
    stop_people = []        
    good_people = []        
    
    report = set(report)
    report = list(report)

    for i in range(len(report)):
        tmp = report[i].split(" ")
        report_people.append(tmp[1])
    
    for i in range(len(id_list)):
        if report_people.count(id_list[i]) >= k:
            stop_people.append(id_list[i])
    
    for i in range(len(report)):
        tmp = report[i].split(" ")
        if stop_people.count(tmp[1]) == 1:
            good_people.append(tmp[0])
    
    for i in range(len(id_list)):
        answer.append(good_people.count(id_list[i]))

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"],3))
