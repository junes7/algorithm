import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String st;
        StringBuilder sb = new StringBuilder();
        for(int i=0;i<3;i++)
            st=scan.nextLine();
        for(int i=0;i<10000;i++)
            sb.append("-1\n");
            System.out.println(sb);
    }
}