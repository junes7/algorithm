import java.util.Scanner;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int arr[] = Arrays.stream(scan.nextLine().split(" "))
        .mapToInt(Integer::parseInt).toArray();
        int idx=0,tar=scan.nextInt();
        String rlt;
        for(int i=0;i<arr.length;i++) {
            if(arr[i]==tar) {
                idx=i+1;
                break;
            }
        }
        if(idx<=5)
            rlt="A+";
        else if(idx<=15)
            rlt="A0";
        else if(idx<=30)
            rlt="B+";
        else if(idx<=35)
            rlt="B0";
        else if(idx<=45)
            rlt="C+";
        else if(idx<=48)
            rlt="C0";
        else
            rlt="F";
        System.out.print(rlt);
    }
}