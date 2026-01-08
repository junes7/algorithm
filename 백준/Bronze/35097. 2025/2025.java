import java.io.BufferedReader;
import java.io.InputStreamReader;
public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int rlt,n;
        while(true) {
            n = Integer.parseInt(br.readLine());
            if(n==0) break;
            rlt=0;
            for(int i=1;i<n+1;i++) {
                for(int j=1;j<n+1;j++) {
                    rlt+=i*j;
                }
            }
            System.out.println(rlt);
        }
    }
}