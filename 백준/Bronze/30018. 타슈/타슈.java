import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;
import java.lang.Math;
public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int rlt=0,n=Integer.parseInt(br.readLine());
        int[] a=Arrays.stream(br.readLine().split(" "))
        .mapToInt(Integer::parseInt).toArray();
        int[] b=Arrays.stream(br.readLine().split(" "))
        .mapToInt(Integer::parseInt).toArray();
        for(int i=0;i<n;i++)
            rlt+=Math.abs(a[i]-b[i]);
        System.out.print(rlt/2);
    }
}