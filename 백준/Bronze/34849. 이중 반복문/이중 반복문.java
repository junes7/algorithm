import java.util.Scanner;
import java.lang.Math;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        long n = Long.parseLong(scan.nextLine());
        System.out.println(n*n/Math.pow(10,8)>1?"Time limit exceeded":"Accepted");
    }
}