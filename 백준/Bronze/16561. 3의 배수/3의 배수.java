import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt()/3;
        System.out.print((n-1)*(n-2)/2);
    }
}