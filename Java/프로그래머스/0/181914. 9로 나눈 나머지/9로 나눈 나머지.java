import java.math.BigInteger;

class Solution {
    public int solution(String number) {
        int answer = 0;
        BigInteger num = new BigInteger(number);
        BigInteger nine = new BigInteger("9");
        return num.remainder(nine).intValue();
    }
}