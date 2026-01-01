import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] dt,cdt=Arrays.stream(br.readLine().split("-"))
        .mapToInt(Integer::parseInt).toArray();
        int cnt=0,n=Integer.parseInt(br.readLine());
        for(int i=0;i<n;i++) {
            dt=Arrays.stream(br.readLine().split("-"))
            .mapToInt(Integer::parseInt).toArray();
            if(dt[0]>cdt[0]) {
                cnt+=1;
            } else if(dt[0]==cdt[0]) {
                if(dt[1]>cdt[1]) {
                    cnt+=1;
                } else if(dt[1]==cdt[1] && dt[2]>=cdt[2]) {
                    cnt+=1;
                }
            }
        }
        System.out.print(cnt);
    }
}