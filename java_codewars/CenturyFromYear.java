import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.LongStream;
import java.util.stream.Stream;




public class CenturyFromYear {

    public static int century(int number) {
        return ((number % 100 == 0))? (number = number / 100 ) :  (number = (number / 100) + 1);
      }


        public static Object[] removeEveryOther(Object[] arr) {  
            List<Object> removeEveryOther = new ArrayList<Object>();
            for (int i = 0; i < arr.length; i = i+2) removeEveryOther.add(arr[i]);
            return removeEveryOther.toArray();
      }
        public static String sayHello(String [] name, String city, String state){
            
            return String.format("Hello, %s! Welcome to %s, %s!", String.join(" ", name),city,state);
  }


   public static String printArray(Object[] array) {

    //Arrays.stream(array).map(Object::toString).collect(Collectors.joining(","));
    return Arrays.stream(array).map(Object::toString).collect(Collectors.joining(","));
    

    //return Arrays.asList(array).toString().replaceAll("(^\\[|\\]$)", "").replace(", ", ",");  
    }

     public static boolean twoArePositive(int a, int b, int c) {

        //return Stream.of(a, b, c).filter(n -> n > 0).count() == 2;

        int[] arr = {a, b, c};
        Arrays.sort(arr);
       return ((arr[1] > 0) & (arr[2] > 0) & (arr[0] <= 0) )  ? true : false;
  }

    public static long eliminateUnsetBits(String number) {
        number = number.replace("0", "");
        return number.isEmpty() ? 0 : Long.parseLong(number, 2);
  }

     static public boolean AmIAfraid(final String day, final int num) {
  
        switch(day){ 
        case "Monday": 
            if (num == 12) return true;
            break; 
        case "Tuesday": 
            if (num > 95) return true;
            break; 
        case "Wednesday": 
            if (num == 34) return true;
            break; 
        case "Thursday": 
            if (num == 0) return true;
            break;
        case "Friday": 
            if (num % 2 == 0 ) return true;
            break;
        case "Saturday": 
           if (num == 56 ) return true;
            break; 
        case "Sunday": 
        if (num == 666 || num == -666) return true;
            break;  
        default: 
            break;
       }
       return false;
    }

       public static long filterString(final String value) {
       return Long.parseLong(value.chars().filter(Character::isDigit).mapToObj(i -> String.valueOf((char) i)).collect(Collectors.joining()));
    }

      public static void main(String[] args) {

        //Integer[] array = new Integer[] { 2, 4, 5, 2 };
         
         //System.out.println(printArray(array));



         //System.out.println(twoArePositive(2, -4, -3));

        System.out.println(filterString("aa1bb2cc3dd"));
         //System.out.println(eliminateUnsetBits("111111111111111111111111111111111"));
        

         // String[] name = {"John", "Smith"};
        //"Hello, John Smith! Welcome to Phoenix, Arizona!"
          ;

       //   System.out.println(sayHello(name, "Phoenix", "Arizona"));

      //  removeEveryOther(new Object[] { "Hello", "Goodbye", "Hello Again" });
    }
    
}
