import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.lang.Math;
public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n1,n2,st = Integer.parseInt(br.readLine());
        while(true) {
            n1=st/100;
            n2=st%100+1;
            st+=1;
            if(st>9999) {
                System.out.print(-1);
                break;
            }
            if(st==Math.pow(n1+n2,2)) {
                System.out.print(st);
                break;
            }
        }
    }
}