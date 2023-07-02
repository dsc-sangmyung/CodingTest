#include <string>
#include <vector>

using namespace std;

int solution(string t, string p) {
    int ans = 0;
    
    for(int i = 0; i < t.size() - p.size() + 1; i++){
        if(t.substr(i, p.size()) <= p) ans++;
    }
    return ans;
}
