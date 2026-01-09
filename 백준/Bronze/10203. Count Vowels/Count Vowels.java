import java.util.*;

public class Main {

    private static int countVowels(String s) {
        int c = 0;
        char vowel[]={'a','e','i','o','u'};
		/* ------------------- INSERT CODE HERE ---------------------*/
        for(int i=0;i<s.length();i++) {
            for(int j=0;j<vowel.length;j++) {
               if(s.charAt(i)==vowel[j]) {
                        c+=1;
                        break;
               }
            }
         }
		/* -------------------- END OF INSERTION --------------------*/
        return c;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int numCases = sc.nextInt();

		for(int i = 0; i < numCases; i++)
		{
			String s = sc.next();
            System.out.println("The number of vowels in " + s + " is " + countVowels(s) + ".");
		}
		
		sc.close();
	}
}
