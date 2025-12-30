import java.io.BufferedReader;
import java.io.InputStreamReader;
public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String st="AKA";
        for(int i=0;i<n;i++)
            st+="RAKA";
        System.out.print(st);
    }
}