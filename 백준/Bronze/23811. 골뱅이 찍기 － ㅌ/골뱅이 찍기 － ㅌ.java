import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        StringBuffer sb = new StringBuffer();
        for(int i=0;i<5;i++) {
            for(int j=0;j<n;j++) {
                if(i%2==0)
                    for(int k=0;k<n*5;k++)
                        sb.append("@");
                else
                    for(int k=0;k<n;k++)
                        sb.append("@");
                sb.append("\n");
            }
        }
        System.out.print(sb.toString());
    }
}