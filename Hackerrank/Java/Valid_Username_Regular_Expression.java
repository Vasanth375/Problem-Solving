import java.util.Scanner;
import java.util.regex.*;
// one case failed
public class Valid_Username_Regular_Expression {
    public static void main(String[] args) {
        // regex pattern // ^[a-zA-Z][a-zA-Z0-9_]{7,29}$
        String regex = "^[a-zA-Z][a-zA-Z0-9_]{7,29}$";
        /*
         * The first character must be a letter, either lowercase or uppercase. This is
         * indicated by the ^[a-zA-Z] part.
         * The following characters can be letters, digits, or underscores. This is
         * indicated by the [a-zA-Z0-9_] part.
         * There must be at least 7 and at most 29 characters after the first one. This
         * is indicated by the {7,29} part.
         * The end of the string must match the end of the pattern. This is indicated by
         * the $ part.
         */
        String actualString = "";
        int i = 0;
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        while (i < n) {
            actualString = scanner.next();
            Pattern pattern = Pattern.compile(regex);
            Matcher matcher = pattern.matcher(actualString);
            if (matcher.matches()) {
                System.out.println("Valid");
            } else {
                System.out.println("Invalid");
            }
            i += 1;
        }
        scanner.close();
    }
}
