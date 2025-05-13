import java.io.*;

class Solution {
    public String solution(String code) {
        String answer = "";
        int mode = 0;
        String[] arr = code.split("");
        for (int i = 0; i<=code.length()-1; i++) {
            if (arr[i].equals("1")) {
                mode = (int)Math.pow(mode-1,2);
            } else if (mode == 0 && i % 2 == 0) {
                answer += arr[i];
            } else if (mode == 1 && i % 2 == 1) {
                answer += arr[i];
            }
        }
        if (answer.equals("")) {
            return "EMPTY";
        }
        return answer;
    }
}