#include <string>
#include <vector>
#include <string.h>

using namespace std;

string solution(string id) {
    string answer = "";
    
    for(int i = 0; i < id.size(); i++){
        id[i] = tolower(id[i]);
        if((id[i] < '0' || id[i] > '9') && (id[i] < 'a' || id[i] > 'z') && !strchr("-_.",id[i])){
            id.erase(i,1);
            i--;
        }
    }
    
    for(int i = 0;i < id.size(); i++){
         if(id[i] == '.'){
            while(id[i + 1] == '.') id.erase(i,1);
        } 
    }
    
    if(id[0] == '.') id.erase(0,1);
    if(id[id.size() - 1] == '.') id.erase(id.size() - 1,1);
    
    if(id.size() == 0) id.append("a");
    else if(id.size() > 15) {
        id.erase(15,id.size() - 15);
        if(id[14] == '.') id.erase(14, 1);
    }
    
    while(id.size() < 3) {
        id.push_back(id[id.size() - 1]);
    }
    
    return id;
}
