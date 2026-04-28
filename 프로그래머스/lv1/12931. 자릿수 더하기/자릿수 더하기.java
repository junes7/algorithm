import java.util.*;

public class Solution {
    public int solution(int n) {
        int rlt = 0;
        while(n>0) {
            rlt+=n%10;
            n/=10;
        }
        return rlt;
    }
}