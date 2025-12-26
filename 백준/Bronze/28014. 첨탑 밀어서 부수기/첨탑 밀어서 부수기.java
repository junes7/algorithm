import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int rlt=1,cur,prev = Integer.parseInt(st.nextToken());
        for(int i=1;i<n;i++) {
            cur = Integer.parseInt(st.nextToken());
            if(prev<=cur) rlt+=1;
            prev=cur;
        }
        System.out.print(rlt);
    }
}