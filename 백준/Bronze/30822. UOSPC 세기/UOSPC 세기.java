import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int tmp,minn=1000,n = Integer.parseInt(scan.nextLine());
        String st = scan.nextLine();
        char tar[]="uospc".toCharArray();
        for(int i=0;i<tar.length;i++) {
            tmp=0;
            for(int j=0;j<st.length();j++) {
                if(st.charAt(j)==tar[i])
                    tmp++;
            }
            if(minn>tmp) minn=tmp;
        }
        System.out.print(minn);
    }
}