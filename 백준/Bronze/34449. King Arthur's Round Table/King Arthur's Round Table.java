import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan=new Scanner(System.in);
        float d = Float.parseFloat(scan.nextLine());
        float w = scan.nextFloat();
        int n = scan.nextInt();
        System.out.println(n<=d/w*3.14159?"YES":"NO");
    }
}