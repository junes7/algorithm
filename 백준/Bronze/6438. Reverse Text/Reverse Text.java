import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringBuffer sb;
        for(int i=0;i<n;i++) {
            sb=new StringBuffer(br.readLine());
            System.out.println(sb.reverse().toString());
        }
    }
}