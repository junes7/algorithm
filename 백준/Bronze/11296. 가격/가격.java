import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Map;
import java.util.HashMap;
public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        Map<String,Double> dic = new HashMap<>();
        dic.put("R",0.55);
        dic.put("G",0.7);
        dic.put("B",0.8);
        dic.put("Y",0.85);
        dic.put("O",0.9);
        dic.put("W",0.95);
        Double ori;
        String dot,vou,pri;
        for(int i=0;i<n;i++) {
            st = new StringTokenizer(br.readLine());
            ori = Double.parseDouble(st.nextToken());
            dot=st.nextToken();
            vou=st.nextToken();
            pri=st.nextToken();
            ori*=dic.get(dot);
            if(vou.equals("C")) {
                ori*=0.95;
            }
            ori*=100;
            if(pri.equals("C")) {
                if(ori%10>5) ori+=10;
                ori-=ori%10;
            }
            System.out.println("$"+String.format("%.2f", ori/100));
        }
    }
}