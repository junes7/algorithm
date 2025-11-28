import java.util.Scanner;
import java.util.Arrays;
public class Main {
    public static void main(String []args) {
        Scanner scan = new Scanner(System.in);
        int cnt=0,n = Integer.parseInt(scan.nextLine());
        for(int i=0;i<n;i++) {
            int[] val=Arrays.stream(scan.nextLine().split(" "))
                        .mapToInt(Integer::parseInt)
                        .toArray();
            if(val[0]>=1000 || val[1]>=1600 || val[2]>=1500 || (1<=val[3]&&val[3]<=30))
                cnt+=1;
        }
        System.out.println(cnt);
    }
}