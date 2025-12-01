import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int d = Integer.parseInt(scan.nextLine());
        int e = Integer.parseInt(scan.nextLine());
        for(int i=0;i<e;i++) {
            String op=scan.nextLine();
            int q=Integer.parseInt(scan.nextLine());
            d=op.equals("+")?d+q:d-q;
        }
        System.out.print(d);
    }
}