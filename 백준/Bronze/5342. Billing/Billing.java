import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
public class Main {
    public static void main(String[] args) throws Exception {
        Map<String,Double> sup = new HashMap<>();
        Double rlt=0.0;
        sup.put("Paper", 57.99);
        sup.put("Printer", 120.50);
        sup.put("Planners", 31.25);
        sup.put("Binders", 22.50);
        sup.put("Calendar", 10.95);
        sup.put("Notebooks", 11.20);
        sup.put("Ink", 66.95);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String st="";
        while((st=br.readLine())!=null)
            rlt+=sup.getOrDefault(st,0.0);
        System.out.print("$"+rlt);
    }
}