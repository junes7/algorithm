import java.util.Scanner;
public class Main {
    public static void main(String []args) {
        Scanner scan = new Scanner(System.in);
        int n = Integer.parseInt(scan.nextLine());
        boolean iskor=false;
        String[] arr = new String[n];
        for(int i=0;i<n;i++) {
            arr[i]=scan.nextLine();
            if(arr[i].equals("korea"))
                iskor=true;
            if(arr[i].equals("yonsei")) {
                System.out.println(iskor?"Yonsei Lost...":"Yonsei Won!");
                break;
            }
        }
    }
}