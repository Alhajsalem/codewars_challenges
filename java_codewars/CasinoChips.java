import java.util.*;

public class CasinoChips {
    public static int solve(int [] arr){
        Arrays.sort(arr);
        int x = arr[0], y = arr[1], z = arr[2];
        int u = (x + y + z) / 2;
        return Math.min(x + y, u);
    }

    public static void main(String[] args) {
        solve(new int[] {1,2,1});
    }
    
}
