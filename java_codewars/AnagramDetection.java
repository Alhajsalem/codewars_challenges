import java.util.stream.Collectors;
import java.util.stream.Stream;

public class AnagramDetection {
    public static boolean isAnagram(String test, String original) {
        return (sortingString(test).equals(sortingString(original)))?  true : false;
      }
    public static String sortingString(String tobeSorted){
        return Stream.of(tobeSorted.toLowerCase().split("")).sorted().collect(Collectors.joining());
    }
      /* return Stream.of(test.toLowerCase().split(""))
                .sorted()
                .collect(Collectors.joining())
                .equals(
                        Stream.of(original.toLowerCase()
                                .split(""))
                                .sorted()
                                .collect(Collectors.joining())); */
      public static void main(String[] args) {
        System.out.println(isAnagram("apple", "pale"));
    }
}
