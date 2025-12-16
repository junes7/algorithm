import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        StringBuffer sb;
        int n = scan.nextInt();
        int k = scan.nextInt();
        int maxn=0,tmp;
        for(int i=0;i<k;i++) {
            sb=new StringBuffer(Integer.toString(n*(i+1)));
            tmp=Integer.parseInt(sb.reverse().toString());
            if(maxn<tmp) maxn=tmp;
        }
        System.out.print(maxn);
    }
}