import java.util.Scanner;
public class Main {
    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        String a=scan.nextLine();
        String b=scan.nextLine();
        int[] rlt={Math.abs(a.charAt(0)-b.charAt(0)),
            Math.abs(a.charAt(1)-b.charAt(1))};
        System.out.print(rlt[0]>rlt[1]?rlt[1]:rlt[0]);
        System.out.print(' ');
        System.out.print(rlt[0]>rlt[1]?rlt[0]:rlt[1]);
    }
}