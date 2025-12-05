import java.util.Scanner;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int total=0,unit[]={100,50,20};
        int price[] = Arrays.stream(scan.nextLine().split(" "))
        .mapToInt(Integer::parseInt).toArray();
        int plan[] = Arrays.stream(scan.nextLine().split(" "))
        .mapToInt(Integer::parseInt).toArray();
        for(int i=0;i<3;i++)
            total+=plan[i]/unit[i]*price[i];
        System.out.println(total);
    }
}