#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int cnt = 0;
    
    for(int i = 1; i <= n; i++){
        cnt++;
        while(cnt % 3 == 0 || to_string(cnt).find("3") != string::npos) cnt++;            
    }
    return cnt;
}
