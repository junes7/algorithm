import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n,m,a,b;
        n = scan.nextInt();
        m = scan.nextInt();
        int cnt[] = new int[n+1];
        for(int i=0;i<m;i++) {
            a = scan.nextInt();
            b = scan.nextInt();
            cnt[a]+=1;
            cnt[b]+=1;    
        }
        for(int i=1;i<n+1;i++)
            System.out.println(cnt[i]);
    }
}