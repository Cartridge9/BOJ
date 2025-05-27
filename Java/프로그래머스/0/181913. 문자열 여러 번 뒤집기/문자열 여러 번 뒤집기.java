class Solution {
    public String solution(String my_string, int[][] queries) {
        String answer = my_string;
        for (int i = 0; i<= queries.length-1; i++) {
            StringBuffer str = new StringBuffer(answer.substring(queries[i][0], queries[i][1]+1));
            answer = answer.substring(0, queries[i][0]) + str.reverse().toString() + answer.substring(queries[i][1]+1);
        }
        return answer;
    }
}