import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        while(true) {
            String word = scan.nextLine();
            if(word.equals("end")) break;
            if(word.equals("animal")) {
                System.out.println("Panthera tigris");
            } else if(word.equals("tree")) {
                System.out.println("Pinus densiflora");
            } else if(word.equals("flower")) {
                System.out.println("Forsythia koreana");
            }
        }
    }
}