public class UsernameValidation {

    /* public static boolean validateUsr(String s) {
        Pattern p = Pattern.compile("^[a-z0-9_]{4,16}$");
        return  p.matcher(s).find();
        } */

        static boolean validateUsr(String s) {
            return s.matches("[a-z0-9_]{4,16}");
          }
    
        public static void main(String[] args) {
            System.out.println(validateUsr("eze-3"));
        }
    
}
