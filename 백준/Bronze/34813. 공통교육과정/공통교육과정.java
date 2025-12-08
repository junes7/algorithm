import java.util.Scanner;
import java.util.HashMap;
import java.util.Map;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String st = scan.nextLine();
        Map<Character,String> rlt=new HashMap<>();
        rlt.put('F',"Foundation");
        rlt.put('C',"Claves");
        rlt.put('V',"Veritas");
        rlt.put('E',"Exploration");
        System.out.print(rlt.get(st.charAt(0)));
    }
}