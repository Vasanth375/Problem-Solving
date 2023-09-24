import java.util.*;

public class Palindrome {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
                
        String B = "";

        // convert the string to char array
        char ch[] = A.toCharArray();
        
        // Code to reverse the string 
        for (int i=A.length()-1; i>= 0; i--){
            B+=ch[i];
        }
        
        // compare two strings
        if (A.compareTo(B) == 0){
            System.out.println("Yes");
        }
        else{
            System.out.println("No");
        }
        sc.close();
    }
}