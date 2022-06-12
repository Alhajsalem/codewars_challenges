public class PlayingBanjo {

    public static String areYouPlayingBanjo(String name) {  
        return String.valueOf(name.charAt(0)).toLowerCase().equals("r") ? name + " plays banjo"  : name + " does not play banjo";    
      }

      public static void main(String[] args) {
        System.out.println(areYouPlayingBanjo("Martin"));
    }
    
}
