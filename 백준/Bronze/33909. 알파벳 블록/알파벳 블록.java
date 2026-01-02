import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.lang.Math;
public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int arr[]=Arrays.stream(br.readLine().split(" "))
        .mapToInt(Integer::parseInt).toArray();
        arr[0]+=arr[3];
        arr[1]+=arr[2]*2;
        System.out.print(Math.min(arr[0]/3, arr[1]/6));
    }
}