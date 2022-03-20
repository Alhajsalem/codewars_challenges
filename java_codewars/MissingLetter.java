import java.util.stream.IntStream;


public class MissingLetter {

    public static char findMissingLetter(char[] array){    
        Object[] letters = IntStream.rangeClosed(array[0],array[array.length-1]).mapToObj(letter -> (char) letter).toArray();
        for(Object item : letters) {
            if (!new String(array).chars().mapToObj(i->(char)i).anyMatch(x -> x == item)){
                return (char) item;
            }
         }
         throw new IllegalArgumentException("Should not happen!");
  }
  public static void main(String[] args) {
    System.out.println(findMissingLetter(new char[] { 'O','Q','R','S' }));
}
    
}
