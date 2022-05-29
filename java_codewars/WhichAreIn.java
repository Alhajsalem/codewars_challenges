import java.util.*;  
public class WhichAreIn {
    public static String[] inArray(String[] array1, String[] array2) {
        Set<String> set = new TreeSet<String>();    
        for (int ii = 0; ii < array1.length; ii++){
            for (int i = 0; i < array2.length; i++) {
                if (array2[i].contains(array1[ii])){
                 set.add(array1[ii]);
                }
        }
    }
    List<String> list = new ArrayList<String>(set);
    return list.toArray(new String[list.size()]); 
   }
/* 
   better solution
   return Arrays.stream(array1)
   .filter(str ->
     Arrays.stream(array2).anyMatch(s -> s.contains(str)))
   .distinct()
   .sorted()
   .toArray(String[]::new); */
   public static void main(String[] args) {
    String a[] = new String[]{ "arp", "live", "strong" };
    String b[] = new String[] { "lively", "alive", "harp", "sharp", "armstrong" };
    String r[] = new String[] { "arp", "live", "strong" };
    System.out.println(inArray(a,b));
} 
    
}
