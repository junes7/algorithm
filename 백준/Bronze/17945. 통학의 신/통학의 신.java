import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.lang.Math;
public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int rlt = (int)Math.sqrt(a*a-b);
        if(rlt>0)
            System.out.print((-a-rlt)+" "+(-a+rlt));
        else
            System.out.print(-a);
    }
}