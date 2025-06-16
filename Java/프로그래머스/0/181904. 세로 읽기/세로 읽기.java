class Solution {
    public String solution(String my_string, int m, int c) {
        String answer = "";
        for (int i = c-1; i<=my_string.length()-1; i+=m) {
            answer += my_string.substring(i, i+1);
        }
        return answer;
    }
}