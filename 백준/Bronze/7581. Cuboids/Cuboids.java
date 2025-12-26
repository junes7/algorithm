import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int l,w,h,v;
        while(true) {
            st = new StringTokenizer(br.readLine());
            l = Integer.parseInt(st.nextToken());
            w = Integer.parseInt(st.nextToken());
            h = Integer.parseInt(st.nextToken());
            v = Integer.parseInt(st.nextToken());
            if(l==0 && w==0 && h==0 && v==0) break;
            if(l==0)
                l=v/(w*h);
            else if(w==0)
                w=v/(l*h);
            else if(h==0)
                h=v/(l*w);
            else
                v=l*w*h;
            System.out.printf("%d %d %d %d\n",l,w,h,v);
        }
    }
}
