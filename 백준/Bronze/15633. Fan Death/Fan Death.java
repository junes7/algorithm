import java.util.Scanner;
import java.lang.Math;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int rlt=0,n = scan.nextInt();
        for(int i=1;i<n+1;i++) {
            if(n%i==0)
                rlt+=i;
        }
        System.out.print(rlt*5-24);
    }
}