import java.lang.Math;

class Solution {
    public int solution(int[] num_list) {
        int sum = 0;
        int mul = 1;
        for (int i = 0; i<= num_list.length-1; i++) {
            sum += num_list[i];
            mul *= num_list[i];
        }
        if (mul > Math.pow(sum, 2)) {
            return 0;
        } else {
            return 1;
        }
    }
}