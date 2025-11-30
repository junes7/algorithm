import java.util.Scanner;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int[] arr=Arrays.stream(scan.nextLine().split(" "))
        .mapToInt(Integer::parseInt).toArray();
        int rlt=arr[0]*3-arr[1];
        System.out.println(rlt>0?rlt*arr[2]+arr[3]:0);
    }
}