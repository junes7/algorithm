import java.util.Scanner;
import java.util.Arrays;
import java.lang.Math;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int maxn,n = Integer.parseInt(scan.nextLine());
        int num[] = Arrays.stream(scan.nextLine().split(" "))
        .mapToInt(Integer::parseInt).toArray();
        int dp[] = new int[n+1];
        dp[0]=num[0];
        maxn=num[0];
        for(int i=1;i<n;i++) {
            dp[i]=Math.max(num[i],num[i]+dp[i-1]);
            if(maxn<dp[i]) maxn=dp[i];
        }
        System.out.print(maxn);
    }
}