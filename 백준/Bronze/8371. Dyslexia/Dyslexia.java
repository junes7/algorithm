import java.io.BufferedReader;
import java.io.InputStreamReader;
public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int rlt=0,n = Integer.parseInt(br.readLine());
        char a[]=br.readLine().toCharArray(),b[]=br.readLine().toCharArray();
        for(int i=0;i<n;i++) {
            if(a[i]!=b[i]) {
                rlt+=1;
            }
        }
        System.out.print(rlt);
    }
}