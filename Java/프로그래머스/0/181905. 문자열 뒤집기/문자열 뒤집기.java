class Solution {
    public String solution(String my_string, int s, int e) {
        String answer = "";
        for (int i = 0; i<=s-1; i++) {
            answer+=my_string.substring(i, i+1);
        }
        for (int i = e; i>=s; i--) {
            answer+=my_string.substring(i, i+1);
        }
        answer+=my_string.substring(e+1);
        return answer;
    }
}