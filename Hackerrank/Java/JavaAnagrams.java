
/**
 * JavaAnagrams
 */
import java.util.*;

public class JavaAnagrams {

    public static void main(String[] args) {
        String a = "Hello";
        String b = "hello";
        anagrams(a, b);
    }

    private static void anagrams(String a, String b) {
        // converting to the lowercase
        a = a.toLowerCase();
        b = b.toLowerCase();

        // character array for sorting purpose
        char aChar[] = a.toCharArray();
        char bChar[] = b.toCharArray();

        // sorting the array
        Arrays.sort(aChar);
        Arrays.sort(bChar);

        // converting back to the string
        a = new String(aChar);
        b = new String(bChar);

        // checking whether the strings are equal or not
        if (a.equals(b)) {
            System.out.println("Anagrams");
        } else {
            System.out.println("Not Anagrams");
        }

    }
}