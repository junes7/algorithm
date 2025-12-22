import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int m = scan.nextInt();
        StringBuilder sb = new StringBuilder();
        for(int i=0;i<n;i++) {
            for(int j=1;j<m;j++) {
                sb.append(i*m+j).append(" ");
            }
            sb.append(i*m+m).append("\n");
        }
        System.out.print(sb.toString());
    }
}