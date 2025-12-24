import java.util.Scanner;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int cnt=0,k = Integer.parseInt(scan.nextLine());
        int n = Integer.parseInt(scan.nextLine());
        int[] a = Arrays.stream(scan.nextLine().split(" "))
        .mapToInt(Integer::parseInt).toArray();
        int m = Integer.parseInt(scan.nextLine());
        int[] b = Arrays.stream(scan.nextLine().split(" "))
        .mapToInt(Integer::parseInt).toArray();
        for(int i=0;i<n;i++) {
            for(int j=0;j<m;j++) {
                if(a[i]+k==b[j])
                    cnt+=1;
            }
        }
        System.out.print(cnt);
    }
}