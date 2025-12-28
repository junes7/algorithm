import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] arr=Arrays.stream(br.readLine().split(" "))
        .mapToInt(Integer::parseInt).toArray();
        for(int a=0;a<arr[0];a++) {
            for(int c=0;c<arr[0];c++) {
                if(arr[2]==(a*arr[1]+c)%arr[0] && arr[3]==(a*arr[2]+c)%arr[0]) {
                    System.out.print(a+" "+c);
                    System.exit(0);
                }
            }
        }
    }
}