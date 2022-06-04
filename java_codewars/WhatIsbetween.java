import java.util.stream.IntStream;

public class WhatIsbetween {

    public static int[] between(int a, int b) {
        //import static java.util.stream.IntStream.rangeClosed;
        //return rangeClosed(a, b).toArray();
        return IntStream.iterate(a, x -> x + 1).takeWhile(x -> x < b+1).toArray();
      }

      public static void main(String[] args) {
        System.out.println(between(1,4));
    }
    
}
