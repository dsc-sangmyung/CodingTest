#include <string>
#include <vector>
#include <map>
using namespace std;

string solution(vector<string> survey, vector<int> choices) {   
    string answer = "";
    
    map<char, int> typeScore;
    int score[8] = {0, 3, 2, 1, 0, 1, 2, 3};

    for(int i = 0; i < survey.size(); i++)
        typeScore[survey[i][choices[i]/4]] += score[choices[i]];
    

    answer += typeScore['R'] >= typeScore['T'] ? 'R' : 'T';
    answer += typeScore['C'] >= typeScore['F'] ? 'C' : 'F';
    answer += typeScore['J'] >= typeScore['M'] ? 'J' : 'M';
    answer += typeScore['A'] >= typeScore['N'] ? 'A' : 'N';
    
    return answer;
}
