import java.util.ArrayList;
import java.util.List;

public class FruitGuy{
 
    public static String[] removeRotten(String[] fruitBasket) {

    //return fruitBasket == null ? new String[0] : Arrays.stream(fruitBasket).map(s -> s.replace("rotten", "").toLowerCase()).toArray(n -> new String[n]);
    
    if (fruitBasket == null) return new String []{};    
    if (fruitBasket.length == 0) return new String []{};
    
    List<String> list = new ArrayList<String>();    
    for (String item : fruitBasket) {
            if (item.contains("rotten")){
                list.add(item.substring("rotten".length(), item.length()).toLowerCase());
            }
            else{
                list.add(item);
            }
    }
    return list.stream().toArray(String[]::new);
    }
    public static void main(String[] args) {
        //String [] expected = new String []{"apple","banana","apple","pineapple","kiwi"};
        String[] rotten = new String []{};
        System.out.println(removeRotten(rotten));
    }
   
   }