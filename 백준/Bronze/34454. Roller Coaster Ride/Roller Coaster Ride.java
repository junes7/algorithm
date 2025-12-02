import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = Integer.parseInt(scan.nextLine());
        int c = Integer.parseInt(scan.nextLine());
        int p = Integer.parseInt(scan.nextLine());
        System.out.println(n>c*p?"no":"yes");
    }
}