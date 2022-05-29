import java.util.*;
import java.util.stream.Collectors;
public class WhereIsMyParent {
    
    public static String findChildren(final String text) {
         return Arrays.stream(text.split("")).sorted().sorted(String.CASE_INSENSITIVE_ORDER).collect(Collectors.joining(""));
    
    }
    public static void main(String[] args) {
        System.out.println(findChildren("abBA"));
    }
}
