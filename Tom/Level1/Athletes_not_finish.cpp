#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(vector<string> p, vector<string> c) {
    string answer = "";

    sort(p.begin(), p.end());
    sort(c.begin(), c.end());

    for(int i = 0; i < c.size(); i++) {
        if(p[i] == c[i]) continue;

        else
            return p[i];
    }

    if(answer == "")
        answer = p[p.size() - 1];
    
    return answer;
}
