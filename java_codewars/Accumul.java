import java.util.ArrayList;
public class Accumul {
    
    public static String accum(String s) {
        ArrayList<String> results = new ArrayList<String>();
        for(int i = 0; i< s.length(); i++){
            results.add(String.valueOf(s.charAt(i)).toUpperCase() + String.valueOf(s.charAt(i)).toLowerCase().repeat(i));
        }
        return String.join("-", results);
    }

/*     var chars = s.split("");

    return IntStream.range(0, chars.length)
            .mapToObj(i -> chars[i].toUpperCase() + chars[i].toLowerCase().repeat(i))
            .collect(Collectors.joining("-"));
 */
    public static void main(String[] args) {
        System.out.println(accum("ZpglnRxqenU"));
    }
	
}