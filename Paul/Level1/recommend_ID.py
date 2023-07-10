# 신규 아이디 추천

import string

def solution(new_id):
    
    lower_new_id = new_id.lower()

    list_new_id = list(map(str, str(lower_new_id)))
    temp_word = ''
    answer = ''
    
    for i in range(len(list_new_id)):
        if list_new_id[i] in string.ascii_lowercase or list_new_id[i] in "-_." or list_new_id[i] in string.digits:
            temp_word = temp_word + list_new_id[i]
    
    while ".." in temp_word:
        temp_word = temp_word.replace('..', ".")

    list_temp_word = list(map(str, str(temp_word)))
    if len(list_temp_word) <= 1:
        if len(list_temp_word) == 0:
            pass
        else:
            if list_temp_word[0] == ".":
                del list_temp_word[0]
    else:
        if list_temp_word[0] == ".":
            del list_temp_word[0]
        if list_temp_word[len(list_temp_word) - 1] == ".":
            del list_temp_word[len(list_temp_word) - 1]

    if len(list_temp_word) == 0:
        list_temp_word.append("a")
    
    if len(list_temp_word) >= 16:
        del list_temp_word[15:]
        if list_temp_word[14] == ".":
            del list_temp_word[14]

    while len(list_temp_word) <= 2:
        list_temp_word.append(list_temp_word[len(list_temp_word) - 1])

    for i in range(len(list_temp_word)):
        answer += list_temp_word[i]

    return answer
