import java.time.LocalDate;
public class AgeInDays {
    public static String ageInDays(int year, int month, int day) {;
        return String.format("You are %d days old", LocalDate.now().toEpochDay() - LocalDate.of(year, month, day).toEpochDay());
      }
    public static void main(String[] args) {
        System.out.println(ageInDays(2015, 11, 1));
    }
    
}
