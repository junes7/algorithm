import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String st = br.readLine().toString();
        char arr[] = st.toCharArray();
        StringBuffer sb = new StringBuffer();
        int cnt=0,idx=0;
        for(int i=arr.length-1;i>=0;i--) {
            if(cnt-3==0) {
                sb.append(',');
                cnt=0;
            }
            sb.append(arr[i]);
            cnt+=1;
        }
        System.out.print(sb.reverse().toString());
    }
}