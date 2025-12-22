import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        StringBuffer sb = new StringBuffer();
        for(int i=0;i<n*5;i++) {
            if(i<n || i>=n*5-n)
                for(int j=0;j<n*5;j++)
                    sb.append("@");
            else
                for(int j=0;j<n;j++)
                    sb.append("@");
            sb.append("\n");
        }
        System.out.print(sb.toString());
    }
}