import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int maxn=0,minn=100,n = Integer.parseInt(scan.nextLine());
        int []arr=new int[n];
        for(int i=0;i<n;i++) {
            arr[i] = Integer.parseInt(scan.nextLine());
            if(maxn<arr[i])
                maxn=arr[i];
            if(minn>arr[i])
                minn=arr[i];
        }
        System.out.println(minn==arr[0]?"ez":maxn==arr[0]?"hard":"?");
    }
}