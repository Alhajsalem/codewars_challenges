import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class DetectPangram {
    public static boolean check(String sentence){
        List<Character> list = new ArrayList<>();
        for (char ch: sentence.toCharArray()) {
            if ((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z')){
                list.add(Character.toUpperCase(ch));
            }
        }
        Set<Character> set1 = list.stream().sorted().collect(Collectors.toSet());
        Character[] letters = IntStream.rangeClosed('A','Z').mapToObj(letter -> (char) letter).toArray(Character[]::new);
        Set<Character> set2 = new HashSet<Character>(Arrays.asList(letters));
        return set1.equals(set2);
      }
    //   return sentence.chars().map(Character::toLowerCase).filter(Character::isAlphabetic).distinct().count() == 26;
      public static void main(String[] args) {
        System.out.println(check("The quick  fox jumps over the lazy dog."));
    }
    
}
