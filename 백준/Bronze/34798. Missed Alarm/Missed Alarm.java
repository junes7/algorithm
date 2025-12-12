import java.util.Scanner;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int t1[]= Arrays.stream(scan.nextLine().split(":"))
        .mapToInt(Integer::parseInt).toArray();
        int t2[]= Arrays.stream(scan.nextLine().split(":"))
        .mapToInt(Integer::parseInt).toArray();
        System.out.println(t1[0]*60+t1[1]<t2[0]*60+t2[1]?"YES":"NO");
    }
}