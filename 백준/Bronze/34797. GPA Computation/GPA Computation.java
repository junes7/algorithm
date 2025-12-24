import java.util.Scanner;
import java.util.HashMap;
import java.util.Map;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int rlt=0,n = Integer.parseInt(scan.nextLine());
        double bn=0;
        Map<Character,Integer> gr=new HashMap<>();
        gr.put('A',4);
        gr.put('B',3);
        gr.put('C',2);
        gr.put('D',1);
        gr.put('E',0);
        String st,tar="ABC";
        for(int i=0;i<n;i++) {
            st=scan.nextLine();
            rlt+=gr.get(st.charAt(0));
            if(tar.indexOf(st.charAt(0))!=-1) {
                if(st.charAt(1)=='1')
                    bn+=0.05;
                else if(st.charAt(1)=='2')
                    bn+=0.025;
            }
        }
        System.out.print((double)rlt/n+bn);
    }
}