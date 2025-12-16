import java.util.Scanner;
import java.lang.Math;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int a,b,n;
        while(true) {
            b = scan.nextInt();
            n = scan.nextInt();
            if(b==0 && n==0) break;
            a=1;
            while(Math.pow(a,n)<b)
                a+=1;
            System.out.println(Math.pow(a,n)-b<b-Math.pow(a-1,n)?a:a-1);
        }
    }
}