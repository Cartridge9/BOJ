class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        String stra = Integer.toString(a);
        String strb = Integer.toString(b);
        answer = (Integer.valueOf(strb + stra) > Integer.valueOf(stra+strb) ? Integer.valueOf(strb + stra) : Integer.valueOf(stra + strb));
        return answer;
    }
}