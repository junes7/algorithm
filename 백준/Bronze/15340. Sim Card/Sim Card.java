import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
public class Main {
    public static void main(String[] args) throws Exception {
        int c,d,rlt,tmp,comp[][]={{30,40},{35,30},{40,20}};
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while(true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            c = Integer.parseInt(st.nextToken());
            d = Integer.parseInt(st.nextToken());
            if(c==0 && d==0) break;
            rlt=100000;
            for(int i=0;i<comp.length;i++) {
                tmp=comp[i][0]*c+comp[i][1]*d;
                if(rlt>tmp) rlt=tmp;
            }
            System.out.println(rlt);
        }
    }
}