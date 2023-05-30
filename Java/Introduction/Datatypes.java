// https://www.hackerrank.com/challenges/java-datatypes/problem?isFullScreen=true

import java.util.*;

class Datatypes {
    public static void main(String[] argh) {
        try (Scanner sc = new Scanner(System.in)) {
            int t = sc.nextInt();
            for (int i = 0; i < t; i++) {
                try {
                    long x = sc.nextLong();
                    System.out.println(x + " can be fitted in:");

                    if (requiredSpace(x) <= 1) {
                        System.out.println("* byte");
                    }
                    if (requiredSpace(x) <= 2) {
                        System.out.println("* short");

                    }
                    if (requiredSpace(x) <= 3) {
                        System.out.println("* int");

                    }
                    if (requiredSpace(x) <= 4) {
                        System.out.println("* long");

                    }
                } catch (Exception e) {
                    System.out.println(sc.next() + " can't be fitted anywhere.");
                }
            }
        }
    }

    private static int requiredSpace(long x) {
        // [-2^7, 2^7-1]
        if (x >= -128 && x <= 127) {
            return 1;
        }
        // [-2^15, 2^15-1]
        else if (x >= -32768 && x <= 32767) {
            return 2;

        }
        // [-2^31, 2^31-1]
        else if (x >= -2147483648 && x <= 2147483647) {
            return 3;

        }
        // [-2^63, 2^64-1]
        else {
            return 4;
        }
    }
}
