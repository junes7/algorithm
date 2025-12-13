import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n,t = scan.nextInt();
        String st;
        for(int i=0;i<t;i++) {
            n = scan.nextInt();
            for(int j=0;j<n;j++) {
                st="";
                for(int k=0;k<n;k++) {
                    if(k==0 || k==n-1) {
                        st+="#";
                    } else {
                        if(1<=j&&j<=n/2) {
                            if(k==j || k==n-1-j)
                                st+="#";
                            else
                                st+=".";
                        } else {
                            st+=".";
                        }
                    }
                }
                System.out.println(st);
            }
        }
    }
}