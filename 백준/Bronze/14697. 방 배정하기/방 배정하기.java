import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int a = scan.nextInt();
        int b = scan.nextInt();
        int c = scan.nextInt();
        int n = scan.nextInt();
        int dp[] = new int[301];
        int tmp,tar[] = {a,b,c};
        dp[a]=dp[b]=dp[c]=1;
        for(int i=a;i<n+1;i++) {
            for(int j=0;j<3;j++) {
                tmp=i-tar[j];
                if(tmp>=0 && dp[tmp]==1) {
                    dp[i]=1;
                }
            }
        }
        System.out.print(dp[n]);
    }
}