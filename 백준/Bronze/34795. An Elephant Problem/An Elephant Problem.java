import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int m = scan.nextInt();
        int d = scan.nextInt();
        System.out.println(d/m+(d%m==0?0:1));
    }
}