import java.util.Scanner;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        int n,k,l;
        Scanner scan = new Scanner(System.in);
        n=scan.nextInt();
        k=scan.nextInt();
        l=n/2+(n%2==0?0:1);
        scan.nextLine();
        int[] arr=Arrays.stream(scan.nextLine().split(" "))
        .mapToInt(Integer::parseInt).toArray();
        for(int i=0;i<k;i++) {
            System.out.print((arr[i]<=l?1:n)+" ");
        }
    }
}