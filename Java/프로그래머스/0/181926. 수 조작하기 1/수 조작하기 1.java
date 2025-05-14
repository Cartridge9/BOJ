class Solution {
    public int solution(int n, String control) {
        int answer = n;
        String[] arr = control.split("");
        for (int i = 0; i<=arr.length-1; i++) {
            switch(arr[i]) {
                case ("w") :
                    n+=1;
                    break;
                case ("s") :
                    n-=1;
                    break;
                case ("d") :
                    n+=10;
                    break;
                case ("a") :
                    n-=10;
                    break;
            }
        }
        return n;
    }
}