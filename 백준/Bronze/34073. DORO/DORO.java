import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n=Integer.parseInt(scan.nextLine());
        String str="";
        String [] arr=scan.nextLine().split(" ");
        for(int i=0;i<n;i++)
            str+=arr[i]+"DORO ";
        System.out.println(str);
    }
}