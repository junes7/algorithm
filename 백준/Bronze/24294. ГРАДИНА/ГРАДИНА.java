import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int w1=scan.nextInt();
        int h1=scan.nextInt();
        int w2=scan.nextInt();
        int h2=scan.nextInt();
        System.out.print(4+(w1>w2?w1:w2)*2+(h1+h2)*2);
    }
}