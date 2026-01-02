import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int c = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        if(c%b==0)
            System.out.print(c/b);
        else
            System.out.print(String.format("%.6f", (double)c/b));
    }
}