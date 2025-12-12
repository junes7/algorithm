import java.util.Scanner;
import java.util.HashMap;
import java.util.Map;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        char ps[];
        int num[]={0,0};
        Map<Character,Integer> rlt=new HashMap<>();
        rlt.put('k',0);
        rlt.put('p',1);
        rlt.put('n',3);
        rlt.put('b',3);
        rlt.put('r',5);
        rlt.put('q',9);
        for(int i=0;i<8;i++) {
            ps=scan.nextLine().toCharArray();
            for(int j=0;j<8;j++) {
                if(ps[j]=='.') continue;
                if(ps[j]>=97)
                    num[1]+=rlt.get(ps[j]);
                else
                    num[0]+=rlt.get((char)(ps[j]+32));
            }
        }
        System.out.print(num[0]-num[1]);
    }
}