import java.util.*;
public class FindAllPairs {

    public static int duplicates(int[] array) {
        int numberPairs = 0;
        Arrays.sort(array);
        for (int i = 0; i < array.length - 1; i++) {
            if (array[i] == array[i + 1]){
                numberPairs++;
                i++;
            }
        }
        return numberPairs;
      }
      public static void main(String[] args) {
        int[] array = new int[]{1, 2, 2, 20, 6, 20, 2, 6, 2};
        int result = duplicates(array);
        System.out.println(result);
    }
}
