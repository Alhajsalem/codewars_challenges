public class RemoveParentheses {

    public static String removeParentheses(final String str) {
        char parentheses_open = '(';
        char parentheses_close = ')';
        int count = 0;
        String result = "";
        for (int i = 0, n = str.length(); i < n; i++) {
            if (str.charAt(i) == parentheses_open) count += 1;  
            if (count == 0) result += str.charAt(i);
            if (str.charAt(i) == parentheses_close) count -= 1;       
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(removeParentheses(" (first group) (second group) (third group)"));
    }
    
}
