import java.util.Scanner;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n=Integer.parseInt(scan.nextLine());
        int arr[] = Arrays.stream(scan.nextLine().split(" "))
        .mapToInt(Integer::parseInt).toArray();
        System.out.print(arr[n-1]+arr[1]-arr[0]);
    }
}