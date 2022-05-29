import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class DaysBetween {
    public static long getDaysAlive(int year, int month, int day, int year2, int month2, int day2) throws ParseException {
        
        SimpleDateFormat myFormat = new SimpleDateFormat("dd MM yyyy");
        Date date1 = myFormat.parse(String.format("%s %s %s", day, month,year));
        Date date2 = myFormat.parse(String.format("%s %s %s", day2, month2,year2));
        long diff = date2.getTime() - date1.getTime();
        return Math.round((diff / (double) 86400000));
    }
    /* better solution 

    import java.time.Duration;
    import java.time.LocalDateTime;
    
    public class DaysBetween {
        public static long getDaysAlive(int year, int month, int day, int year2, int month2, int day2) {
            LocalDateTime date1 = LocalDateTime.of(year, month, day, 0, 0);
            LocalDateTime date2 = LocalDateTime.of(year2, month2, day2, 0, 0);
            Duration duration = Duration.between(date1, date2);
            return duration.toDays();
    
        }
    }   */  
    public static void main(String[] args) {
        
        try {
            System.out.println(getDaysAlive(2005, 10, 27, 2017, 4, 6));
        } catch (ParseException e) {
            e.printStackTrace();
        }
    }
    
}
