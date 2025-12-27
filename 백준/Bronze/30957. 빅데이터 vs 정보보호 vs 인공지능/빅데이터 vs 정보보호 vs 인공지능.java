import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int maxn=0,n = Integer.parseInt(st.nextToken());
        String rlt="",tmp="BSA",str = br.readLine().toString();
        int num[]=new int[3];
        for(int i=0;i<3;i++) {
            for(int j=0;j<n;j++)
                if(str.charAt(j)==tmp.charAt(i))
                    num[i]+=1;
            if(maxn<num[i]) maxn=num[i];
        }
        if(num[0]==num[1] && num[1]==num[2] && num[0]==num[2]) {
            rlt+="SCU";
        } else {
            for(int k=0;k<3;k++) {
                if(num[k]==maxn)
                    rlt+=tmp.charAt(k);
            }
        }
        System.out.print(rlt);
    }
}