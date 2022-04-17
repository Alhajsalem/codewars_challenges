
public class AlphabetSymmetry {
    public static int[] solve(String[] arr){
        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        int newarr[] = new int[arr.length];
        int counter = 0;
        for (int ii = 0; ii < arr.length; ii++){
            int result = (arr[ii].length() > alphabet.length()) ? alphabet.length(): arr[ii].length();
            for (int i = 0; i < result; i++) {
                if (arr[ii].toLowerCase().charAt(i) == alphabet.charAt(i)){
                    counter+=1;
                }
        }
        newarr[ii] = counter;
        counter = 0;
    }
       return newarr; 
    }
  /*   better solution
    public static String alphabet = "abcdefghijklmnopqrstuvwxyz";

    public static int countLetters(String str) {
        return IntStream.range(0, str.length()).filter(i -> alphabet.indexOf(str.charAt(i)) == i).toArray().length;
    }

    public static int[] solve(String[] arr){
        return Stream.of(arr).map(String::toLowerCase).mapToInt(Solution::countLetters).toArray();
    } */

    public static void main(String[] args) {
        System.out.println(solve(new String[]{"abcdefghijklmnopqrstuvwxyzr","ABc","xyzD"}));
    }
    
}
