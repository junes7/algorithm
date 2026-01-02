import java.io.BufferedReader;
import java.io.InputStreamReader;
public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine(),t = br.readLine(),rlt="";
        Boolean exist;
        for(int i=0;i<t.length();i++) {
            exist=false;
            for(int j=0;j<s.length();j++) {
                if(s.charAt(j)==t.charAt(i)) {
                    exist=true;
                    break;
                }
            }
            if(!exist) rlt+=t.charAt(i);
        }
        System.out.print(rlt);
    }
}