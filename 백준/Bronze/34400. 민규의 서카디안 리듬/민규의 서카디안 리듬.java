import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int t,n=scan.nextInt();
        for(int i=0;i<n;i++) {
            t=scan.nextInt();
            System.out.println(t%25<17?"ONLINE":"OFFLINE");
        }
    }
}