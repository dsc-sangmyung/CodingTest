#include <string>
#include <vector>

using namespace std;

int solution(int chicken) {
    int rest = 0, ans = 0;
    
    while(chicken >= 10){                
        ans += chicken / 10;
        chicken = chicken /10 + chicken % 10;
    }
    
    return ans;
}
