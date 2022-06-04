public class Ghostbusters {

    public static String ghostBusters(String building) {
        return building.contains(" ") ? building.replace(" ", "") : "You just wanted my autograph didn't you?";
      }
    public static void main(String[] args) {
        System.out.println(ghostBusters("O  f fi ce"));
    }
    
}
