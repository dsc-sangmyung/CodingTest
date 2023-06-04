#include <string>
#include <vector>

using namespace std;

int solution(int a, int b) {  
    int ans = 1, end;
    end = a > b ? a : b;
    
    for(int i = 2; i <= end; i++){
        if((a % i == 0) && (b % i == 0)) ans = max(ans, i);
    }
    
    b = b / ans;

    int i = 2;
    
    while(i <= b) {
        if(b % i == 0){
            if(i != 2 && i != 5) return 2;
            b /= i;
        }
        else i++;
    }
       
    return 1;
}
