#include <vector>
#include <map>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    map<string, int> m;
    map<string, int>::iterator iter;
    
    for(int i = 0; i < participant.size(); i++){
        if(!m.size() || m.find(participant[i]) == m.end()) m.insert(pair<string, int>(participant[i], 1));
        else ++m[participant[i]];
    }
    
    for(int i = 0; i < completion.size(); i++){
        iter = m.find(completion[i]);
        if(m[completion[i]] > 1) --m[completion[i]];
        else m.erase(iter);
    }
    
    return m.begin() -> first;
}
