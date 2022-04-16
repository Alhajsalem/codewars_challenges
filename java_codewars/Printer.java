public class Printer {

    public static String printerError(String s) {
        int controlStringLength = s.length();
        int numberOfErrors = 0;
        for (char currentChar : s.toCharArray()) {
          if (currentChar > 'm'){
            numberOfErrors++;
          }
        }
        return numberOfErrors + "/" + controlStringLength;    
    
    }
/* 
    long errs = s.chars().filter( ch -> ch > 'm').count();
    return errs+"/"+s.length(); */

    public static void main(String[] args) {
        System.out.println(printerError("aaabbbbhaijjjm"));
    }



    
}
