public class HashString {
    public static void main(String[] args) {
        String str = "#Capgemini#is#the#best#company";
        String hash = "";
        String words = "";
        int i;
        for(i=0; i < str.length(); i++) {
            if(str.charAt(i) == '#') {
                hash = hash + str.charAt(i);
            }
            else{
                words += str.charAt(i);
            }
        }
        System.out.println("Hashes: " + hash+words);
    }
}
