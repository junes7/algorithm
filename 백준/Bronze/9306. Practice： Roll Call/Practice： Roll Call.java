import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = Integer.parseInt(scan.nextLine());
        String[] names = new String[n*2];
        for(int i=0;i<n;i++) {
            names[2*i] = scan.nextLine();
            names[2*i+1] = scan.nextLine();
        }
        for(int i=0;i<n;i++) {
            System.out.println("Case "+(i+1)+": "+names[2*i+1]+", "+names[2*i]);
        }
    }
}