import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String tmp;
        StringBuffer sb = new StringBuffer();
        int n = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());
        for(int i=0;i<n;i++) {
            tmp=br.readLine().toString();
            sb.setLength(0);
            for(int j=0;j<n;j++) {
                if(tmp.charAt(j)=='d')
                    sb.append(d==1?'q':'b');
                else if(tmp.charAt(j)=='b')
                    sb.append(d==1?'p':'d');
                else if(tmp.charAt(j)=='q')
                    sb.append(d==1?'d':'p');
                else
                    sb.append(d==1?'b':'q');
            }
            System.out.println(sb.toString());
        }
    }
}