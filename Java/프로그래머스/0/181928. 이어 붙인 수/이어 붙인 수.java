import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.lang.Math;
import java.lang.Integer;

class Solution {
    public int solution(int[] num_list) {
        int odd = 0;
        int even = 0;

        for (int i=num_list.length-1; i>=0; i--) {
            if (num_list[i] % 2 ==0) {
                even += num_list[i] * (int)Math.pow(10, Integer.toString(even).length());
                System.out.println("even : " + even);
            } else {
                System.out.println(Integer.toString(odd).length());
                odd += num_list[i] * (int)Math.pow(10, Integer.toString(odd).length());
                System.out.println("odd : " + odd);
            }
        }
        return (even+odd)/10;
    }
}