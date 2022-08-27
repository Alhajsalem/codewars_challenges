public class CenturyFromYear {

    public static int century(int number) {
        return ((number % 100 == 0))? (number = number / 100 ) :  (number = (number / 100) + 1);
      }

      public static void main(String[] args) {
          System.out.println(century(1601));
    }
    
}
