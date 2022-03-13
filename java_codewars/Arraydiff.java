import java.util.stream.IntStream;
import java.util.*;

public class Arraydiff {
    public static int[] arrayDiff(int[] a, int[] b) {
        List<Integer> list = new ArrayList<>();
        for(int item : a) {
           if (!IntStream.of(b).anyMatch(x -> x == item)){
               list.add(item);
           }
        }
        return list.stream().mapToInt(Integer::intValue).toArray();
      }
      
      /* return IntStream.of(a).filter(x -> IntStream.of(b).noneMatch(y -> y == x)).toArray(); */

      public static void main(String[] args) {
        System.out.println(arrayDiff(new int[] {1, 2, 2, 2, 3}, new int[] {2}));
    }
}
