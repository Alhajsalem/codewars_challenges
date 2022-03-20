import java.util.stream.Collectors;
import java.util.*;
public class  StringToCamelCase {

    static String toCamelCase(String s){
        if(s.length() == 1) return s;
        String result = Arrays.stream(s.replaceAll("[-_]","_").split("_")).map(i -> i.substring(0, 1).toUpperCase() + i.substring(1)).collect(Collectors.joining(""));
        return s.substring(0, 1).toLowerCase()+ result.substring(1);
      }
      
   /*    String[] words = str.split("[-_]");
      return Arrays.stream(words, 1, words.length)
              .map(s -> s.substring(0, 1).toUpperCase() + s.substring(1))
              .reduce(words[0], String::concat); */

    public static void main(String[] args) {
    String input = "the_Stealth-Warrior";
      System.out.println("input: "+input);      
      System.out.println(StringToCamelCase.toCamelCase(input));
    }
	
    
}
