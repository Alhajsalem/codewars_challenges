import java.util.Arrays;

public class FormatWord {

    public static String formatWords(String[] words) {
        if(words == null || words.length == 0) return "";
        String [] filteredWords = Arrays.stream(words).filter(word -> word != "").toArray(String[]::new);
        System.out.println(Arrays.toString(filteredWords));
        if (filteredWords.length >= 3){
            return String.format("%s and %s", String.join(", ", Arrays.copyOfRange(filteredWords, 0, filteredWords.length-1)),filteredWords[filteredWords.length-1]);
        }
        else if(filteredWords.length == 2){
            return String.format("%s and %s", filteredWords[0], filteredWords[1]);
        }
        else if(filteredWords.length == 1){
            return String.format("%s", filteredWords[0]);
        }
        return "";  
      }

   /*    better solution
      if (words == null) return "";
      String ans = Arrays.stream(words).filter( s -> !s.isEmpty() ).collect(Collectors.joining(", "));
      return ans.replaceAll(", ([^,]+)$", " and $1"); */

       public static void main(String[] args) {
        System.out.println(formatWords(new String[] {"", "cpjxk","" , "qbjudqt", "jp"}));
    }
}
