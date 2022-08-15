import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Sid {

  /*   public static String howMuchILoveYou(int nb_petals) {
    
        String[] arr ={"not at all", "I love you",  "a little", "a lot", "passionately", "madly"};
      
        return arr[nb_petals%6];
      } */

    public static String howMuchILoveYou(int nb_petals) {
        Map<String, String> myMap = new HashMap<String, String>();
        myMap.put("0", "not at all");
        myMap.put("1", "I love you");
        myMap.put("2", "a little");
        myMap.put("3", "a lot");
        myMap.put("4", "passionately");
        myMap.put("5", "madly");
        return myMap.get(String.valueOf(nb_petals%6));
        }
      public static <T> int[] unique(int[] integers) {

        //Integer[] boxedArray = IntStream.of(integers).boxed().toArray(Integer[]::new);

        LinkedHashSet<Integer> hashSet = IntStream.of(integers).boxed().collect(Collectors.toCollection(LinkedHashSet::new));
        return hashSet.stream().mapToInt(Number::intValue).toArray();
        }    

        /*       import java.util.*;

        public class UniqueArray {
        public static int[] unique(int[] integers) {
            Set<Integer> set = new LinkedHashSet<Integer>();
            for(int i: integers){
            set.add(i);
            }
            return set.stream().mapToInt(i->i).toArray();
        }
        } */
        public static void main(String[] args) {
            int[] duplicatesInOrder1 = new int[]{1, 3, 2, 3, 2, 1, 2, 3, 1, 1, 3, 2};
            System.out.println(unique(duplicatesInOrder1));
        }
}
