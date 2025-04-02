import java.util.List;
import java.util.ArrayList;

public class GenerateParanthesis {

    public static void generateParanthesis(int n, int open, int close, StringBuilder sb, List<String> result) {
        if (open == n && close == n) {
            result.add(sb.toString());
            // System.out.println(sb.toString());
            return;
        }
        if (open < n) {
            sb.append("(");
            generateParanthesis(n, open + 1, close, sb, result);
            sb.deleteCharAt(sb.length() - 1);
        }
        if (close < open) {
            sb.append(")");
            generateParanthesis(n, open, close + 1, sb, result);
            sb.deleteCharAt(sb.length() - 1);
        }
    }

    public static void main(String[] args) {
        int n = 3;
        List<String> result = new ArrayList<>();
        int open = 0, close = 0;
        StringBuilder sb = new StringBuilder();
        generateParanthesis(n, open, close, sb, result);
        System.out.println(result);
    }
}