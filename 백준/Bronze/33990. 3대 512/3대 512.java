import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int minn=600,tot,rlt=0,n = Integer.parseInt(br.readLine()),arr[];
        for(int i=0;i<n;i++) {
            arr=Arrays.stream(br.readLine().split(" "))
            .mapToInt(Integer::parseInt).toArray();
            tot=Arrays.stream(arr).sum();
            if(tot-512>=0) {
                if(minn>tot-512) {
                    minn=tot-512;
                    rlt=tot;
                }
            }
        }
        System.out.print(rlt>0?rlt:-1);
    }
}