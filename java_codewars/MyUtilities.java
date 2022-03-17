public class MyUtilities {

    public static boolean isDigit(String s){
        try {
            Float.parseFloat(s);
            } catch (NumberFormatException ex) {
            return false;
            }    
      return true;  
  }
  public static void main(String[] args) {
    System.out.println(isDigit("  3  "));
}
    
}
