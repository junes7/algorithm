import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int a = scan.nextInt();
        int t = scan.nextInt();
        int rlt = 10+2*(25-a+t);
        System.out.print(rlt<0?0:rlt);
    }
}