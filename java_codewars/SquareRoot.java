import java.util.*;
public class SquareRoot {
    public static int[] squareOrSquareRoot(int[] array){
        List<Integer> list = new ArrayList<>();
        Arrays.stream(array).forEach(no -> {
            int b = (int) Math.sqrt(no);
            if (no == Math.pow(b, 2)){ 
                list.add((int)Math.sqrt(no));
            }
            else{
                list.add(no*no);
            }
        });      
      return list.stream().mapToInt(Integer::intValue).toArray();
    }
/*     better solution
    return Arrays.stream(array)
    .map(i -> Math.sqrt(i) % 1 == 0 ? ((int) Math.sqrt(i)) : (i * i))          
    .toArray();   */    

    public static void main(String[] args) {
        System.out.println(squareOrSquareRoot(new int[] {100, 101}));
    }   
}
