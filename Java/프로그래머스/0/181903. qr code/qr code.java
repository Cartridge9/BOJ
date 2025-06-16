class Solution {
    public String solution(int q, int r, String code) {
        String answer = "";
        for (int i = 0; i<=code.length()-1; i++) {
            if (i%q == r) {
                answer += code.substring(i, i+1);
            }
        }
        return answer;
    }
}