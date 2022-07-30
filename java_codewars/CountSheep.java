public class CountSheep {

    public static String countingSheep(int num) {
        String result = "";
        for(int i = 1; i <= num; i++){
           result += String.valueOf(i) +" sheep...";
        }
        return result;
      }
/*       public static String countingSheep(int num) {
        StringBuilder stringBuilder = new StringBuilder();
        for (int i = 1; i <= num; i++) {
            stringBuilder.append(i).append(" sheep...");
        }
        return stringBuilder.toString();
    } */

 /*    public class Kata {
        public static String countingSheep(int num) {
          return IntStream.rangeClosed(1, num)
                          .mapToObj(i -> i + " sheep...")
                          .collect(Collectors.joining());
        } */

       
  public static boolean zeroFuel(double distanceToPump, double mpg, double fuelLeft) {
    return (mpg * fuelLeft >= distanceToPump);
  }   
      public static void main(String[] args) {
        //1 sheep...2 sheep...3 sheep...", Kata.countingSheep(3)
        //1 sheep...2 sheep...3 sheep...
        countingSheep(3);
    }

    
}
