import java.util.Scanner;
import java.util.Arrays;
import java.lang.Math;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        long[] arr=Arrays.stream(scan.nextLine().split(" "))
        .mapToLong(Long::parseLong).toArray();
        System.out.println(Math.min(arr[2]*arr[1],arr[2]*(arr[1]+1)*(100-arr[0])/100));
    }
}