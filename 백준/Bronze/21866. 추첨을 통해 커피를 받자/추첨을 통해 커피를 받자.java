import java.util.Scanner;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int[] arr = Arrays.stream(scan.nextLine().split(" "))
        .mapToInt(Integer::parseInt).toArray();
        int[] maxn={100,100,200,200,300,300,400,400,500};
        int hac=0,total=0;
        for(int i=0;i<9;i++) {
            if(arr[i]>maxn[i]) {
                hac=1;
                break;
            }
            total+=arr[i];
        }
        System.out.print(hac==1?"hacker":(total>=100?"draw":"none"));
    }
}