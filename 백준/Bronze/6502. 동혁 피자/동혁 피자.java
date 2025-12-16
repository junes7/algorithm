import java.util.Scanner;
import java.lang.Math;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int cnt=1;
        while(true) {
            int r = scan.nextInt();
            if(r==0) break;
            int w = scan.nextInt();
            int l = scan.nextInt();
            System.out.printf("Pizza %d %s on the table.\n",cnt++,2*r>=Math.sqrt(w*w+l*l)?"fits":"does not fit");
        }
    }
}