import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Bigdecimaljava {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        List<String> list = new ArrayList<String>();
        for (int i = 0; i < n; i++) {
            list.add(sc.next());
        }

        // Sort using BigDecimal for numerical comparison in descending order
        list.sort((a, b) -> {
            BigDecimal num1 = new BigDecimal(a);
            BigDecimal num2 = new BigDecimal(b);

            // Descending order: compare b to a
            return num2.compareTo(num1);
        });
        list.forEach(System.out::println);
        sc.close();
    }
}