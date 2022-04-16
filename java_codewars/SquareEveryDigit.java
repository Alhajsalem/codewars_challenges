import java.util.*;
public class SquareEveryDigit {
    public static int squareDigits(int n) {
       List<Integer> myList = new ArrayList<Integer>();
       String[] digits = Integer.toString(n).split("");
       for(String d : digits){
        myList.add(Integer.parseInt(d)*Integer.parseInt(d));
       }
       System.out.println(myList);
       String listString = "";

       for (Integer s : myList)
       {
           listString += s;
       }
       return Integer.parseInt(listString);
      }
      public static void main(String[] args) {
        System.out.println(squareDigits(9119));
    }
    
}
