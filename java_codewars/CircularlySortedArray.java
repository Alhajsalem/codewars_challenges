public class CircularlySortedArray {

    public static boolean isCircleSorted(int[] a) {
        boolean result = false;
        for (int i = 1; i < a.length; ++i) {
            if (a[i - 1] > a[i]) {
                if (result) return false;
                result = true;
            }
        }

        if (result && a[a.length - 1] > a[0]) return false;
        return true;
    }


  public static void main(String[] args) {
    int[] A={2, 3, 4, 5, 0, 1};
    System.out.println(isCircleSorted(A));
}
    
}
