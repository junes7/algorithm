import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan=new Scanner(System.in);
        int a,b;
        String c;
        a=scan.nextInt();
        b=scan.nextInt();
        c=scan.nextLine();
        if((c.charAt(c.length()-1)-48)%2!=0)
            System.out.print(a^b);
        else
            System.out.print(a);
    }
}