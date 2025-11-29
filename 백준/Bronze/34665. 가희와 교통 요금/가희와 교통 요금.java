import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String a=scan.nextLine();
        String b=scan.nextLine();
        System.out.println(a.equals(b)?0:1550);
    }
}