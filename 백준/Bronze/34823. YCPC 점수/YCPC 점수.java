import java.util.Scanner;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int rlt;
        int [] n=Arrays.stream(scan.nextLine().split(" "))
        .mapToInt(Integer::parseInt).toArray();
        rlt=n[0]<n[1]/2?n[0]:n[1]/2;
        System.out.print(n[2]<rlt?n[2]:rlt);
    }
}