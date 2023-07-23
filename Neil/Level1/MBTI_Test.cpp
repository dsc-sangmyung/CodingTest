#include <string>
#include <vector>

using namespace std;

string solution(vector<string> survey, vector<int> choices) {
    string ans = "RCJA";
    int point[8] = {0, 3, 2, 1, 0, 1, 2, 3};
    char type[4] = {'T', 'F', 'M', 'N'};
    vector<pair<int, int>> mbti(4, make_pair(0,0));
    
    for(int i = 0; i < survey.size(); i++) {
        string s = survey[i];
        string c;
        
        if(choices[i] == 4) continue;
        else if(1 <= choices[i] && choices[i] <= 3) c = s[0];
        else c = s[1];
        
        if(c == "R" || c == "C" || c == "J" || c == "A") {
            int idx;
            if(c == "R") idx = 0;
            else if(c == "C") idx = 1;
            else if(c == "J") idx = 2;
            else idx = 3;
            
            mbti[idx].first += point[choices[i]];
        }
        
        else {
            int idx;
            if(c == "T") idx = 0;
            else if(c == "F") idx = 1;
            else if(c == "M") idx = 2;
            else idx = 3;
            
            mbti[idx].second += point[choices[i]];
        }
    }
    
    for(int i = 0; i < 4; i++) {
        if(mbti[i].first < mbti[i].second) ans[i] = type[i];
    }
    return ans;
}
