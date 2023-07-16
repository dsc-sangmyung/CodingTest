class Solution {
    fun solution(new_id: String): String {
        var id: String = new_id
        // lv1
        id = id.toLowerCase()
        
        // lv2
        var temp = StringBuilder()
        val regex = Regex("[a-z0-9-_.]")
        for(i in id.indices) {
            if(regex.containsMatchIn(id[i].toString())){
                temp.append(id[i])
            }
        }
        id = temp.toString()
        
        // lv3
        id = id.replace(Regex("[.]*[.]"), ".")
        
        // lv4
        id = id.removePrefix(".").removeSuffix(".")
        
        // lv5
        if(id.isEmpty()) {
            id = "a"
        }
        
        // lv6
        if(id.length >= 16) {
            id = id.substring(0..14)
        }
        id = id.removeSuffix(".")
        
        // lv7
        while (id.length <= 2) {
            id = id + (id[id.length-1])
        }
        
        var answer: String = id
        return answer
    }
}
