class Solution {
    public String solution(String my_string, String overwrite_string, int s) {     
        String[] lista = my_string.split("");
        String[] listb = overwrite_string.split("");
        
        for (int i = 0; i < overwrite_string.length(); i++) {
            lista[i+s] = listb[i];
        }
        
        return String.join("", lista);
    }
}