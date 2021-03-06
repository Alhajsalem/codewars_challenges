import java.util.stream.IntStream;



public class Multiples3or5 {
    public static int solution(int number) {
    int sum=0;
    for (int i=0; i < number; i++){
      if (i%3==0 || i%5==0){sum+=i;}
    }
    return sum;
  }
  public static int betterSolutin(int number){
    return IntStream.range(0, number)
    .filter(n -> (n % 3 == 0) || (n % 5 == 0))
    .sum();
  }
      public static void main(String[] args) {
        System.out.println(solution(10));
    }      
}

