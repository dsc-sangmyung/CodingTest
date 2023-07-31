#include <algorithm>
#include <vector>

using namespace std;

vector<int> solution(vector<string> id_list, vector<string> report, int k) {
    int size = id_list.size();
    
    vector<int> cnt(size);
    vector<int> result(size, 0);
    
    // 신고 가능 횟수를 1회씩 부여
    vector<vector<bool>> chance(size, vector<bool>(size, true));
    
    for(int i = 0; i < report.size(); i++) {
        string p1 = ""; // 신고 한 사람
        string p2 = ""; // 신고 당한 사람
        
        int j;
        for(j = 0; report[i][j] != ' '; j++)
            p1 += report[i][j];
        p2 = report[i].substr(j + 1);
        
        auto it1 = find(id_list.begin(), id_list.end(), p1);
        auto it2 = find(id_list.begin(), id_list.end(), p2);
        
        int idx1 = it1 - id_list.begin();
        int idx2 = it2 - id_list.begin();
        
        if(!chance[idx1][idx2]) continue;
        
        cnt[idx2]++;
        chance[idx1][idx2] = false;
    }
    
    for(int i = 0; i < cnt.size(); i++) {
        if(cnt[i] < k) continue;
        
        for(int j = 0; j < size; j++){
            if(!chance[j][i]) result[j]++;
        }
    }
     
    return result;
}
