import java.util.Arrays;

public class JadenCase {

    public static String toJadenCase(String phrase) {
       if(phrase == null || phrase.length() == 0) return null;
       String [] results = Arrays.stream(phrase.split(" ")).map(name -> name.substring(0, 1).toUpperCase() + name.substring(1)).toArray(String[]::new);
       return String.join(" ", results);
    }

/*     public String toJadenCase(String phrase) {
        if (null == phrase || phrase.length() == 0) {
            return null;
        }
  
        return Arrays.stream(phrase.split(" "))
                     .map(i -> i.substring(0, 1).toUpperCase() + i.substring(1, i.length()))
                     .collect(Collectors.joining(" "));
    } */


/*     public static final Collector<CharSequence,?,String> JOIN_WITH_SPACE = Collectors.joining(" ");

    public String toJadenCase(String phrase) {
      if (phraseIsEmpty(phrase)) { return null; }
      
      return Arrays.stream(splitIntoWords(phrase)).map(this::capitalize).collect(JOIN_WITH_SPACE);
    }
  
    private String[] splitIntoWords(String phrase) {
      return phrase.split(" ");
    }
    
    private String capitalize(String word) {
      return word.substring(0, 1).toUpperCase() + word.substring(1);
    }
    
    private boolean phraseIsEmpty(String phrase) {
      return phrase == "" || phrase == null;
    } */
    public static void main(String[] args) {
        System.out.println(toJadenCase(null));
    }
    
    
}
