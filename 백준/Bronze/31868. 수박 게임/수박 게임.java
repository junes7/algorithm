import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int arr[]=Arrays.stream(br.readLine().split(" "))
        .mapToInt(Integer::parseInt).toArray();
        for(int i=0;i<arr[0]-1;i++)
            arr[1]/=2;
        System.out.print(arr[1]);
    }
}