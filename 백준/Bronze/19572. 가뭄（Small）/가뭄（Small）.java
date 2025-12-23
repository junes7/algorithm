import java.util.Scanner;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int[] d = Arrays.stream(scan.nextLine().split(" "))
        .mapToInt(Integer::parseInt).toArray();
        double sumn,a,b,c;
        sumn=(d[0]+d[1]+d[2])/2.0;
        a=sumn-d[2];
        b=sumn-d[1];
        c=sumn-d[0];
        if(a>0 && b>0 && c>0) {
            System.out.println(1);
            System.out.print(a+" "+b+" "+c);
        } else
            System.out.print(-1);
    }
}