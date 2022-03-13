import java.util.stream.Stream;
import java.util.*;

public class SpinWords {
    public static String spinWords(String sentence) {
        List<String> list = new ArrayList<>();
        Stream.of(sentence.split(" ")).forEach(
            word -> {
                if (word.length() >= 5){   
                    list.add(new StringBuilder(word).reverse().toString());
                }
                else  {
                    list.add(word);
                }
            }
        );
        return String.join(" ", list);
    }

   /*  return Arrays.stream(sentence.split(" "))
    .map(i -> i.length() > 4 ? new StringBuilder(i).reverse().toString() : i)
    .collect(Collectors.joining(" ")); */
    
    public static void main(String[] args) {
        System.out.println(spinWords("Hey fellow warriors"));
    }   
    
}
