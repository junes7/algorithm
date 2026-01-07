import java.io.BufferedReader;
import java.io.InputStreamReader;
public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int arr[]=new int[n];
        arr[0]=1;
        arr[1]=2;
        arr[n-1]=997;
        for(int i=1;i<n;i++) {
            if(arr[i]==0)
                arr[i]=arr[i-1]+1;
        }
        System.out.println(n);
        for(int i=0;i<n;i++)
            System.out.print(arr[i]+" ");
    }
}