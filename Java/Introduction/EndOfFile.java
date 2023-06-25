// https://www.hackerrank.com/challenges/java-end-of-file/problem?isFullScreen=true

import java.util.Scanner;

public class EndOfFile {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int cnt = 1;
        while (scanner.hasNext()) {
            String line = scanner.nextLine();

            System.out.println(cnt + " " + line);
            cnt++;
        }

        scanner.close();
    }
}
