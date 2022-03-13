import java.util.*;
import java.util.stream.Collectors;


public class FindOdd {

    public static int findIt(int[] a) {
        Map<Object, Long> counts   = Arrays.stream(a).boxed().collect(Collectors.toList()).stream().collect(Collectors.groupingBy(e -> e, Collectors.counting()));
        int result = 0;
        for (var entry : counts.entrySet()) {
            if (entry.getValue() % 2 != 0){ 
                System.out.println((int) entry.getKey());
                result = (int) entry.getKey();
            }
        }
        return result;
    }
    public static void main(String[] args) {
        int result = findIt(new int[]{20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5});
        System.out.println(result);
    }
}
