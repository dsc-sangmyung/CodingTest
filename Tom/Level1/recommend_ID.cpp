#include <string>
#include <vector>
#include <iostream>
#include <regex>

using namespace std;

string solution(string new_id) {    
    // 1단계
    for (int i = 0; i < new_id.size(); i++)
        new_id[i] = tolower(new_id[i]);
    
    // 2단계
    new_id = regex_replace(new_id, regex("[^a-z0-9-_.]+"), "");
    
    // 3단계
    new_id = regex_replace(new_id, regex("[.]+"), ".");
    
    // 4단계
    if (new_id[0] == '.')
        new_id.erase(new_id.begin());
    
    if (new_id[new_id.length() - 1] == '.')
        new_id.erase(new_id.end() - 1);
    
    // 5단계
    if (new_id.length() == 0)
        new_id = "a";
    
    // 6단계
    if (new_id.length() >= 16) {
        new_id.erase(15);
        if (new_id[new_id.length() - 1]=='.')
            new_id.erase(new_id.end() - 1);
    }
    
    // 7단계
    if (new_id.length() <= 2){
        char temp = new_id[new_id.length() - 1];
        
        for (int i = new_id.size(); i < 3; i++)
            new_id += temp;
    }
    
    return new_id;
}
