import java.util.Scanner;
import java.lang.Math;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int l = scan.nextInt();
        System.out.print(0.5*l*l*Math.sin(120*Math.PI/180));
    }
}