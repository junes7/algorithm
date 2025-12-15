import java.util.Scanner;
import java.lang.Math;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int a,b,t = scan.nextInt();
        for(int i=0;i<t;i++) {
            a = scan.nextInt();
            b = scan.nextInt();
            System.out.println((int)Math.pow(a/b, 2));
        }
    }
}