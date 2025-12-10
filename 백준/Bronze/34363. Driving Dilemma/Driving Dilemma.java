import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int s = scan.nextInt();
        double d = scan.nextDouble();
        double t = scan.nextDouble();
        System.out.print(d/(s*5280/3600)<=t?"MADE IT":"FAILED TEST");
    }
}