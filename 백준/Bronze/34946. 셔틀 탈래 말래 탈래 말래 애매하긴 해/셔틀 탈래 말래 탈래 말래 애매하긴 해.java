import java.util.Scanner;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int[] arr=Arrays.stream(scan.nextLine().split(" "))
        .mapToInt(Integer::parseInt).toArray();
        String st;
        if(arr[0]+arr[1]>arr[3] && arr[2]>arr[3])
            st="T.T";
        else {
            if(arr[2]>arr[3])
                st="Shuttle";
            else if(arr[0]+arr[1]>arr[3])
                st="Walk";
            else
                st="~.~";
        }
        System.out.print(st);
    }
}