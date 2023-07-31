def solution(id_list, report, k):
    report_list = []
    answer = [0 for a in range(len(id_list))]
    
    for user in id_list:
        user_report_temp = []
        for r in report:
            r_split = r.split()
            if r_split[1] == user:
                if r_split[0] not in user_report_temp:
                    user_report_temp.append(r_split[0])
        report_list.append(user_report_temp)
        
    for a in report_list:
        if len(a) >= k:
            for var in a:
                answer[id_list.index(var)] += 1
    
    return answer
