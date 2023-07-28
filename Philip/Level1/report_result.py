def solution(id_list, report, k):
    a = []
    report = set(report)
    request = [0] * len(id_list)
    result = [0] * len(id_list)
    
    for i in report:
        a = i.split()
        request[id_list.index(a[1])] += 1
    for i in report:
        a = i.split()
        if(request[id_list.index(a[1])] >= k):
            result[id_list.index(a[0])] += 1
    return result
