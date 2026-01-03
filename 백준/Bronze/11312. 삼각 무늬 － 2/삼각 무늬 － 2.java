import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        long arr[];
        for(int i=0;i<t;i++) {
            arr=Arrays.stream(br.readLine().split(" "))
            .mapToLong(Long::parseLong).toArray();
            System.out.println((arr[0]/arr[1])*(arr[0]/arr[1]));
        }
    }
}