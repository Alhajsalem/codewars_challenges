public class HowManyPagesInABook {

    public static int amountOfPages(int summary) {   
        String result = "";
        for(int i = 1; i< summary; i++){
            result = result + String.valueOf(i);
            if (result.length() == summary) return i;
        }
        return summary;
      }



    public static void main(String[] args) {
        System.out.println(amountOfPages(5));
    }
    
}
