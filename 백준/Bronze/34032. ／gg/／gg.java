import java.io.BufferedReader;
import java.io.InputStreamReader;
public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int cnt=0,mid,n = Integer.parseInt(br.readLine());
        String st = br.readLine();
        mid=n/2+(n%2==0?0:1);
        for(int i=0;i<st.length();i++) {
            if(st.charAt(i)=='O')
                cnt+=1;
        }
        System.out.print(cnt>=mid?"Yes":"No");
    }
}