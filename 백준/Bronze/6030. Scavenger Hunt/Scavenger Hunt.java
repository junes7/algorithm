import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int idxp=0,p = Integer.parseInt(st.nextToken());
        int idxq=0,q = Integer.parseInt(st.nextToken());
        int []pe=new int[p];
        int []qe=new int[q];
        for(int i=1;i<p+1;i++) {
            if(p%i==0)
                pe[idxp++]=i;
        }
        for(int i=1;i<q+1;i++) {
            if(q%i==0)
                qe[idxq++]=i;
        }
        for(int i=0;i<idxp;i++) {
            for(int j=0;j<idxq;j++)
                System.out.println(pe[i]+" "+qe[j]);
        }
    }
}