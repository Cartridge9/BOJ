class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[queries.length];
        for (int i = 0; i<=queries.length-1; i++) {
            for (int j = queries[i][0]; j<=queries[i][1]; j++) {
                if (j == queries[i][0]) {
                    answer[i] = -1;
                }
                
                if (answer[i] == -1 && arr[j] > queries[i][2]) {
                    answer[i] = arr[j];
                    continue;
                }
                
                if (answer[i] > arr[j] && arr[j] > queries[i][2]) {
                    answer[i] = arr[j];
                }
            }
        }
        return answer;
    }
}