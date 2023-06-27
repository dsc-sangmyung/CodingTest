#include <string>
using namespace std;

int solution(string t, string p) {
    int t_len = t.length();
    int p_len = p.length();
    
    int ans = 0;
    
    for(int i = 0; i <= t_len - p_len; i++)
        if (stol(t.substr(i, p_len)) <= stol(p))
            ans++;
    
    return ans;
}
