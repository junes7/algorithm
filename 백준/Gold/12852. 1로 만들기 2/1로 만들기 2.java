import java.util.Scanner;
import java.lang.Math;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int idx=0,tmp,now,x = scan.nextInt();
        int rlt[],dp[] = new int[x+1];
        for(int i=2;i<x+1;i++) {
            dp[i]=dp[i-1]+1;
            if(i%3==0)
                dp[i]=Math.min(dp[i],dp[i/3]+1);
            if(i%2==0)
                dp[i]=Math.min(dp[i],dp[i/2]+1);
        }
        System.out.println(dp[x]);
        rlt=new int[dp[x]+1];
        rlt[idx++]=x;
        tmp=dp[x]-1;
        now=x;
        for(int i=x;i>=0;i--) {
            if(dp[i]==tmp && (i+1==now || i*2==now || i*3==now)) {
                now=i;
                rlt[idx++]=i;
                tmp-=1;
            }           
        }
        for(int i=0;i<rlt.length;i++)
            System.out.print(rlt[i]+" ");
    }
}