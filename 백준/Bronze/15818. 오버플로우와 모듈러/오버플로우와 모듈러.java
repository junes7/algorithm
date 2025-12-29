import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        long rlt=1;
        int[] arr = Arrays.stream(br.readLine().split(" "))
        .mapToInt(Integer::parseInt).toArray();
        for(int i=0;i<n;i++) {
            rlt*=arr[i];
            rlt%=m;
        }
        System.out.print(rlt);
    }
}