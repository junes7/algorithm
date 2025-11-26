import java.util.Scanner;
public class Main {
    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        int n = Integer.parseInt(scan.nextLine());
        StringBuilder sb=new StringBuilder();
        String []p_list={"G...",".I.T","..S."};
        for(int i=0;i<p_list.length;i++) {
            char []elem=p_list[i].toCharArray();
            sb.setLength(0);
            for(int j=0;j<p_list[i].length();j++) {
                for(int k=0;k<n;k++) {
                    sb.append(elem[j]);
                }
            }
            for(int j=0;j<n;j++) {
                System.out.println(sb.toString());
            }
        }
    }
}