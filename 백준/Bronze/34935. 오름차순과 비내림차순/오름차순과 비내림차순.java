import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        boolean rlt=true;
        long[] arr = new long[n];
        arr[0]=scan.nextLong();
        for(int i=1;i<n;i++) {
            arr[i]=scan.nextLong();
            if(arr[i-1]>=arr[i]) {
                rlt=false;
                break;
            }
        }
        System.out.print(rlt?1:0);
    }
}