// https://www.hackerrank.com/challenges/java-strings-introduction/problem?isFullScreen=true

import java.util.Scanner;

public class StringsIntroduction {
    public static final String capitalize(String str) {
        if (str == null || str.length() == 0) {
            return str;
        }
        return str.substring(0, 1).toUpperCase() + str.substring(1);
    }

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            String A = sc.next();
            String B = sc.next();
            /* Enter your code here. Print output to STDOUT. */
            System.out.println(A.length() + B.length());
            System.out.println(A.compareTo(B) > 0 ? "Yes" : "No");
            System.out.println(capitalize(A) + " " + capitalize(B));
        }
    }
}
