import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int elem,n = scan.nextInt();
        boolean rlt=true;
        for(int i=0;i<n;i++) {
            elem=scan.nextInt();
            if(elem<48) {
                rlt=false;
                break;
            }
        }
        System.out.println(rlt?"True":"False");
    }
}