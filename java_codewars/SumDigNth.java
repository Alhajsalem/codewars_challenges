
// https://www.codewars.com/kata/55ffb44050558fdb200000a4/train/java
public class SumDigNth {

    public static long sumDigNthTerm(long initval, long[] patternl, int nthterm) {
        
        final int n = patternl.length;
        int sum = (int) initval;
        for(int z = 0; z <= nthterm-2; z++){
            sum += (int) patternl[(z % n)]; 
        }
        return String.valueOf(sum).chars().map(Character::getNumericValue).sum(); 
    }

    public static void main(String[] args) {
        System.out.println(sumDigNthTerm(10, new long[] {2, 1, 3}, 6));
    }
    
}
