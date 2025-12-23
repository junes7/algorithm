import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        StringBuffer sb = new StringBuffer();
        for(int i=0;i<n*5;i++) {
            if(i<n) {
                for(int j=0;j<n*3;j++)
                    sb.append("@");
                for(int j=0;j<n;j++)
                    sb.append(" ");
                for(int j=0;j<n;j++)
                    sb.append("@");
            } else if(n<=i && i<n*5-n) {
                for(int j=0;j<5;j++) {
                    for(int k=0;k<n;k++)
                        sb.append(j%2==0?"@":" ");
                }
            } else {
                for(int j=0;j<n;j++)
                    sb.append("@");
                for(int j=0;j<n;j++)
                    sb.append(" ");
                for(int j=0;j<n*3;j++)
                    sb.append("@");
            }
            sb.append("\n");
        }
        System.out.print(sb.toString());
    }
}