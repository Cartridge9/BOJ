import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        for (char x : a.toCharArray()) {
            if(x>=97 && x<=122){
                x = (char)(x-32);
                System.out.print(x);
            }else{
            	x = (char)(x+32);
                System.out.print(x);
            }
        }
    }
}