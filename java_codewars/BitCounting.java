import java.util.*;
public class BitCounting {
    public static int countBits(int n){
        return (int) Arrays.stream((Integer.toBinaryString(n)).split("")).filter(x -> (x.equals("1"))).count();
    }
    public static void main(String[] args) {
        System.out.println(countBits(1234));
    }
	
    
}
