public class BreakcamelCase {
    public static String camelCase(String input) {
        String[] camelCaseWords = input.split("(?=[A-Z])");
        return  String.join(" ", camelCaseWords);
      }

      public static void main(String[] args) {
        System.out.println(camelCase("camelCasingTest"));
    }
    
}
