class Solution {
    public int solution(int n) {
        int t=0,a=1,b=1;
        for(int i=3;i<n+1;i++) {
            t=a;
            a=b;
            b=(t+b)%1234567;
        }  
        return b;
    }
}