import java.util.*;

public class CreatePhoneNumber {

    public static String createPhoneNumber(int[] numbers) {
       
        return String.format("(%s) %s-%s",getString(numbers, 0, 3),getString(numbers, 3, 6),getString(numbers, 6, numbers.length));
      }
     public static StringBuilder getString(int[] numbers, int start, int end){
        int[] intArray = Arrays.copyOfRange(numbers, start, end);

        StringBuilder stringBuilder = new StringBuilder();
        for (int i = 0; i < intArray.length; i++) {
            stringBuilder.append(intArray[i]);
        }
        return stringBuilder;
     } 

    public static void main(String[] args) {
        System.out.println(createPhoneNumber(new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}));
    }
    
}
