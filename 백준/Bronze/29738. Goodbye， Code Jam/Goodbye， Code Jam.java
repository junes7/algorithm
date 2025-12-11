import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n,t = scan.nextInt();
        String rlt;
        for(int i=0;i<t;i++) {
            n=scan.nextInt();
            rlt="Round 1";
            if(n<=25) rlt="World Finals";
            else if(n<=1000) rlt="Round 3";
            else if(n<=4500) rlt="Round 2";
            System.out.println("Case #"+(i+1)+": "+rlt);
        }
    }
}