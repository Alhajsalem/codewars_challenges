import java.util.stream.Stream;
import java.util.*;

public class DeadFish {
    public static int[] parse(String data) {
        int[] counter = new int[1];
        List<Integer> list = new ArrayList<>();
        Stream.of(data.toLowerCase().split("")).forEach(
            value -> {
                if (value.equals("i")){   
                    counter[0]++;
                }
                else if  (value.equals("s")){
                    counter[0]*=counter[0];
                }
                else if  (value.equals("d")){
                    counter[0]--;
                }
                else if (value.equals("o")){
                    list.add(counter[0]);
                }
            }
        );
        return list.stream().mapToInt(Integer::intValue).toArray();
    }
    public static void main(String[] args) {
        System.out.println(parse("iiisdoso"));
    }
    
}
