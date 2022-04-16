
public class StringyStrings {

    public static String stringy(int size) {
        if (size %2 == 0) return "10".repeat(size/2);
        return "10".repeat((size/2)+1);

      }
      public static void main(String[] args) {
        System.out.println(stringy(15));
    }
}
