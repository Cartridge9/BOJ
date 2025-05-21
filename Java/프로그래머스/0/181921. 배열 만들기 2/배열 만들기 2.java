import java.util.ArrayList;
import java.lang.Integer;
import java.util.List;
import java.util.Arrays;

class Solution {
    public int[] solution(int l, int r) {
        List<Integer> arr = new ArrayList<>();
        for (int i = l; i <= r; i++) {
            String[] list = Integer.toString(i).split("");
            for (int j = 0; j <= list.length-1; j++) {
                if(list[j].equals("5") || list[j].equals("0")) {
                    if (j == list.length-1) {
                        arr.add(Integer.parseInt(String.join("", list)));
                    }
                } else {
                    break;
                }
            }
        }
        int[] arr2 = {-1};
        if (arr.size() != 0) {
            arr2 = arr.stream()
                .mapToInt(Integer::intValue)
                .toArray();
        }
        return arr2;
    }
}