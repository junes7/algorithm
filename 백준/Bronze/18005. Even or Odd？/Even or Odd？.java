import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n=scan.nextInt();
        System.out.print(n%2==1?0:(n/2%2==0?2:1));
    }
}