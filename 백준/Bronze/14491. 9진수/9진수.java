import java.util.Scanner;
public class Main {
    public static String solve(String r,int n) {
        if(n==0) return r;
        return solve((n%9!=0?Integer.toString(n%9):"0")+r,n/9);
    }
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        System.out.print(solve("",n));
    }
}