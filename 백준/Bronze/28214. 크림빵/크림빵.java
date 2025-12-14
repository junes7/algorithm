import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int k = scan.nextInt();
        int p = scan.nextInt();
        int elem,cnt,rlt=0;
        for(int i=0;i<n;i++) {
            cnt=0;
            for(int j=k*i;j<k*(i+1);j++) {
                elem = scan.nextInt();
                if(elem==0)
                    cnt+=1;
            }
            if(cnt<p)
                rlt+=1;
        }
        System.out.print(rlt);
    }
}