import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n,d,v,f,c,cnt,t=Integer.parseInt(br.readLine());
        for(int i=0;i<t;i++) {
            st=new StringTokenizer(br.readLine());
            n=Integer.parseInt(st.nextToken());
            d=Integer.parseInt(st.nextToken());
            cnt=0;
            for(int j=0;j<n;j++) {
                st=new StringTokenizer(br.readLine());
                v=Integer.parseInt(st.nextToken());
                f=Integer.parseInt(st.nextToken());
                c=Integer.parseInt(st.nextToken());
                if(v*f/c>=d) cnt+=1;
            }
            System.out.println(cnt);
        }
    }
}