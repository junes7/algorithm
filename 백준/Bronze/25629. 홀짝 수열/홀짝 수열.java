import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.lang.Math;
public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        int rlt[] = new int[2];
        int arr[]=Arrays.stream(br.readLine().split(" "))
        .mapToInt(Integer::parseInt).toArray();
        for(int i=0;i<n;i++) {
            if(arr[i]%2!=0)
                rlt[0]+=1;
            else
                rlt[1]+=1;
        }
        System.out.print(rlt[0]==Math.ceil(n/2.0) && rlt[1]==n/2?1:0);
    }
}