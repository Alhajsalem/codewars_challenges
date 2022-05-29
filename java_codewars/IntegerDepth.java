import java.util.*;
public class IntegerDepth {

    public static int computeDepth(int n) {
       Set<String> setA = new HashSet<>();
       int i = 0;
       while (true) {
           String [] result = String.valueOf(n*i++).split("");
           for(String anObject : result) setA.add(anObject);
         if(setA.size() == 10) return i;  
       }   
    }

    public static void main(String[] args) {
        System.out.println(computeDepth(478));
    }
    
}
