import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int fibo[] = new int[n+1];
        fibo[1]=fibo[2]=1;
        for(int i=3;i<n+1;i++)
            fibo[i]=fibo[i-1]+fibo[i-2];
        System.out.print(fibo[n]+" "+(n-2));
    }
}