import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int w = scan.nextInt();
        int rlt = 10*n;
        if(n==5)
            rlt+=70;
        else if(n>=3)
            rlt+=20;
        if(w>1000)
            rlt = rlt-15<0?0:rlt-15;
        System.out.println(rlt);
    }
}