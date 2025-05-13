import java.lang.Math;
import java.util.Arrays;

class Solution {
    public int solution(int a, int b, int c) {
        int answer = 0;
        int[] list = {a, b, c};
        int[] arr = Arrays.stream(list).distinct().toArray();
        
        if (arr.length == 3) {
            answer += a+b+c;
        } else if (arr.length == 2) {
            answer += (a + b + c) * (int)(Math.pow(a,2) + Math.pow(b, 2) + Math.pow(c, 2));
        } else if (arr.length == 1) {
            answer += (a + b + c) * (Math.pow(a,2) + Math.pow(b, 2) + Math.pow(c, 2)) * (Math.pow(a,3) + Math.pow(b, 3) + Math.pow(c, 3));
        }
        return answer;
    }
}