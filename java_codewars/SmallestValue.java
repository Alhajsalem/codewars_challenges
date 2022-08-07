import java.util.Arrays;
import java.util.stream.Collectors;

public class SmallestValue {

    public static int findSmallest( final int[] numbers, final String toReturn ) {
        switch(toReturn){
            case "value":
            return Arrays.stream(numbers).min().orElse(0);
            case "index":
            return Arrays.stream(numbers).boxed().collect(Collectors.toList()).indexOf(Arrays.stream(numbers).min().orElseThrow());
        }
        return 1;
        }

        public static void main(String[] args) {
            System.out.println(SmallestValue.findSmallest( new int [] {7, 12, 3, 2, 27} , "value") );

        }
    
}
