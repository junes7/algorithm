import java.util.Scanner;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int b,s,rlt=0;
        double l;
        int m[]=Arrays.stream(scan.nextLine().split(" "))
        .mapToInt(Integer::parseInt).toArray();
        int n = scan.nextInt();
        for(int i=0;i<n;i++) {
            b=scan.nextInt();
            l=scan.nextDouble();
            s=scan.nextInt();
            if(l>=2.0 && s>=17)
                rlt+=m[b];
        }
        System.out.print(rlt);
    }
}