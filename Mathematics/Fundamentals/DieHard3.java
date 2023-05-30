import java.io.*;
import java.util.stream.*;

class Result {

    public static boolean solve(int cup1, int cup2, int target) {
        return target <= Math.max(cup1, cup2) && target % gcd(cup1, cup2) == 0;
    }

    private static int gcd(int a, int b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }

}

public class DieHard3 {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int t = Integer.parseInt(bufferedReader.readLine().trim());

        IntStream.range(0, t).forEach(tItr -> {
            try {
                String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");
                int a = Integer.parseInt(firstMultipleInput[0]);
                int b = Integer.parseInt(firstMultipleInput[1]);
                int c = Integer.parseInt(firstMultipleInput[2]);

                boolean result = Result.solve(a, b, c);

                bufferedWriter.write(result ? "YES" : "NO");
                bufferedWriter.newLine();
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        bufferedReader.close();
        bufferedWriter.close();
    }
}
