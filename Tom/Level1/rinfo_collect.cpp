#include <string>
#include <vector>
using namespace std;

bool func(string today ,vector<string> terms, string p) {
    char t = p[p.length() - 1]; // 동의한 약관 알파벳
    string period; // 약관 기간

    for (int i = 0; i < terms.size(); i++) {
        if (t == terms[i][0]) {
            for (int j = 2; j < terms[i].length(); j++)
                period += terms[i][j];
        }
    }

    // 각 동의한 약관 날짜에서 년, 월, 일 int형으로 추출
    int year = stoi(p.substr(0, 4));
    int month = stoi(p.substr(5, 2));
    int date = stoi(p.substr(8, 2));

    // 동의 날짜 + 약관 기간
    month += stoi(period);

    // 12월까지 있으니까, 12월 넘어가는거 계산 (주의, month가 12 이하가 되도록 계속 빼줘야댐!)
    while (month > 12) {
        month -= 12;
        year++;
    }

    // 현재 날짜에서 년, 월, 일 int형으로 추출
    int t_year = stoi(today.substr(0, 4));
    int t_month = stoi(today.substr(5, 2));
    int t_date = stoi(today.substr(8, 2));

    // 현재년도 > 유효년도
    if (t_year > year) return false;
    // 같은 년인 경우, month 비교도 필요함....
    else if (t_year == year && t_month > month) return false;
    // 같은 년, 월인 경우, date 비교도 필요함....
    else if (t_year == year && t_month == month && t_date >= date) return false;

    return true;
}

vector<int> solution(string today, vector<string> terms, vector<string> privacies) {
    vector<int> answer;

    for (int i = 0; i < privacies.size(); i++)
        if (!func(today, terms, privacies[i]))
            answer.push_back(i + 1);
  
    return answer;
}
