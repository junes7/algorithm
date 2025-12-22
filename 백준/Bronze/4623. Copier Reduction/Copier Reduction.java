import java.util.Scanner;
import java.util.Arrays;
public class Main {
    private static void swap(int[] arr) {
        int tmp;
        tmp=arr[0];
        arr[0]=arr[1];
        arr[1]=tmp;
    }
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int[] arr,arr1,arr2;
        int s,e,mid,rlt=0;
        boolean fit;
        while(true) {
            arr=Arrays.stream(scan.nextLine().split(" "))
            .mapToInt(Integer::parseInt).toArray();
            if(arr[0]==0 && arr[1]==0 && arr[2]==0 && arr[3]==0) break;
            arr1 = new int[]{arr[0],arr[1]};
            arr2 = new int[]{arr[2],arr[3]};
            if(arr1[0]<arr1[1]) swap(arr1);
            if(arr2[0]<arr2[1]) swap(arr2);
            s=1;e=100;
            while(s<=e) {
                mid=(s+e)/2;
                fit=(arr1[0]*mid>arr2[0]*100||arr1[1]*mid>arr2[1]*100)?false:true;
                if(fit) {
                    s=mid+1;
                    rlt=mid;
                } else
                    e=mid-1;
            }
            System.out.println(rlt+"%");
        }
    }
}