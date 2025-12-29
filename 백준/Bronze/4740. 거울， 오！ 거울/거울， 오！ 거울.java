import java.io.BufferedReader;
import java.io.InputStreamReader;
public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String st;
        while(true) {
            st=br.readLine();
            if(st.equals("***")) break;
            System.out.println(sb.append(st).reverse());
            sb.setLength(0);
        }
    }
}