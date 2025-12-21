import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int idx=0,h = scan.nextInt();
        String st="";
        if(h<2) {
            System.out.print(h==1?0:1);
        } else {
            for(int i=0;i<h%2;i++)
                st+='4';
            for(int i=0;i<h/2;i++)
                st+='8';
            System.out.print(st);
        }
    }
}