import java.math.BigInteger;
import java.util.Scanner;

/**
 * Java_BigInteger
 */
public class Java_BigInteger {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        BigInteger a = sc.nextBigInteger();
        BigInteger b = sc.nextBigInteger();
        BigInteger add = a.add(b);
        BigInteger mul = a.multiply(b);
        System.out.println(add + "\n" + mul);
        sc.close();
    }
}