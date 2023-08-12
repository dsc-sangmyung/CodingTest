# 개인정보 수집 유효기간

def dateToDay(date):
    year, month, day = map(int, date.split("."))

    return (year * 12 * 28) + (month * 28) + day

def solution(today, terms, privacies):

    answer = []
    terms_two = []
    privacies_two = []
    count = 0

    for index in privacies:
        privacies_two.append(list(map(str, index.split(" "))))

    for index in terms:
        terms_two.append(list(map(str, index.split(" "))))

    for index_privacies in privacies_two:
        count += 1

        for index_terms in terms_two:

            if index_terms[0] == index_privacies[1]:
                temp_list = list(map(int, index_privacies[0].split(".")))
                terms_days = int(index_terms[1]) * 28
                temp_list[2] += terms_days - 1

                if temp_list[2] + temp_list[1] * 28 + temp_list[0] * 12 * 28 < dateToDay(today):
                    answer.append(count)

    return answer

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))
