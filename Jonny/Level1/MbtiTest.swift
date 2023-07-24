import Foundation

func solution(_ survey:[String], _ choices:[Int]) -> String {
    var score = ["R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0,  "N": 0]
    var answer = ""
    
    for i in 0..<survey.count {
        let a = String(survey[i].first!)
        let b = String(survey[i].last!)
        
        if choices[i] >= 1 && choices[i] <= 3 {
            score[a]! += (4 - choices[i])
        } else if choices[i] >= 5 && choices[i] <= 7 {
            score[b]! += (choices[i] - 4)
        }
    }
    
    score["R"]! >= score["T"]! ? answer.append("R") : answer.append("T")
    score["C"]! >= score["F"]! ? answer.append("C") : answer.append("F")
    score["J"]! >= score["M"]! ? answer.append("J") : answer.append("M")
    score["A"]! >= score["N"]! ? answer.append("A") : answer.append("N")
    
    return answer
}
