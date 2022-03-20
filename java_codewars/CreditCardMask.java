public class CreditCardMask {
    public static String maskify(String str) {
        return str.replaceAll(".(?=.{4})", "#");
    }

    public static void main(String[] args) {
        System.out.println(maskify("4556364607935616"));
    }
}
