public class leetcode69 {
    public static int mySqrt(int x) {
        if (x == 0 || x == 1) {
            return x; // The square root of 0 is 0, and the square root of 1 is 1.
        }

        int left = 0, right = x;
        int result = 0;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            // Check if mid * mid is less than or equal to x
            if ((long) mid * mid <= x) {
                result = mid; // Store mid as the potential answer
                left = mid + 1; // Narrow the range to higher values
            } else {
                right = mid - 1; // Narrow the range to lower values
            }
        }

        return result; // The square root rounded down
    }

    public static void main(String[] args) {
        // Test cases
        int x1 = 4;
        int x2 = 8;
        int x3 = 0;
        int x4 = 1;

        System.out.println("The square root of " + x1 + " is " + mySqrt(x1));
        System.out.println("The square root of " + x2 + " is " + mySqrt(x2));
        System.out.println("The square root of " + x3 + " is " + mySqrt(x3));
        System.out.println("The square root of " + x4 + " is " + mySqrt(x4));
    }
}
