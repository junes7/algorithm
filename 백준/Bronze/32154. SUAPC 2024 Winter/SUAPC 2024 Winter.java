import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int rlt[][]={
            {1,2,3,4,5,6,7,8,10,12,13},
            {1,3,5,6,7,8,9,12,13},
            {1,3,5,6,7,8,9,12,13},
            {1,2,3,5,6,7,8,12,13},
            {1,3,5,6,7,8,12,13},
            {1,3,5,6,7,8,12,13},
            {1,3,5,6,7,8,12,13},
            {1,3,5,6,7,8,12,13},
            {1,3,5,6,7,8,12,13},
            {1,2,3,6,7,8,12,13}
        };
        int l=rlt[n-1].length;
        System.out.println(l);
        for(int i=0;i<l;i++)
            System.out.print((char)(rlt[n-1][i]+64)+" ");
    }
}