import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int tmp,prev=1000,rlt=0,n = scan.nextInt();
        for(int i=0;i<n;i++) {
            tmp=scan.nextInt();
            if(prev>=tmp)
                prev=tmp;
            else
                rlt+=tmp-prev;
        }
        System.out.print(rlt);
    }
}