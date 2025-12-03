import java.util.Scanner;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int []arr= Arrays.stream(scan.nextLine().split(" "))
        .mapToInt(Integer::parseInt).toArray();
        System.out.println(arr[1]/arr[0]<2?"take it":"double it");
    }
}