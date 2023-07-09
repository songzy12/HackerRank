// https://www.hackerrank.com/challenges/java-string-compare/problem?isFullScreen=true

import java.util.Scanner;

public class SubstringComparisons {

    public static String getSmallestAndLargest(String s, int k) {
        String smallest = s.substring(0, k);
        String largest = s.substring(0, k);

        for (int i = k + 1; i <= s.length(); ++i) {
            String tmp = s.substring(i - k, i);
            if (smallest.compareTo(tmp) > 0) {
                smallest = tmp;
            }
            if (largest.compareTo(tmp) < 0) {
                largest = tmp;
            }
        }

        return smallest + "\n" + largest;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();

        System.out.println(getSmallestAndLargest(s, k));
    }
}
