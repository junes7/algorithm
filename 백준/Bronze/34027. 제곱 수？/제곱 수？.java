import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.lang.Math;
public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n,t = Integer.parseInt(br.readLine());
        double tmp;
        for(int i=0;i<t;i++) {
            n = Integer.parseInt(br.readLine());
            tmp = Math.sqrt(n);
            System.out.println(tmp==(int)tmp?1:0);
        }
    }
}