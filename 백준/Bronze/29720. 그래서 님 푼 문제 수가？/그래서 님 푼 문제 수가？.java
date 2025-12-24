import java.util.Scanner;
import java.util.Arrays;
import java.lang.Math;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int[] arr=Arrays.stream(scan.nextLine().split(" "))
        .mapToInt(Integer::parseInt).toArray();
        System.out.print(Math.max(arr[0]-arr[1]*arr[2], 0)+" "+(arr[0]-(arr[1]*(arr[2]-1))-1));
    }
}