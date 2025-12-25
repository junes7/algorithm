import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int yr,n = scan.nextInt();
        String sub;
        for(int i=0;i<n;i++) {
            sub=scan.next();
            yr=scan.nextInt();
            if(yr==2026) {
                System.out.print(sub);
                break;
            }
        }
    }
}