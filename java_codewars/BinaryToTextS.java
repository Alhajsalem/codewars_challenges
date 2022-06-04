import java.util.*;

public class BinaryToTextS {

    public static String binaryToText(String binary) {
        if (binary.length() < 8) return binary;
        StringBuilder result = new StringBuilder();
        Arrays.stream(binary.split("(?<=\\G.{8})")).forEach(s -> {
            result.append((char) Integer.parseInt(s, 2));
        });
        return result.toString();
      }

      public static void main(String[] args) {
        System.out.println(binaryToText("0100100001100101011011000110110001101111"));
    }
    
}
