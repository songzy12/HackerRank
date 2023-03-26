import java.util.*;

public class OutputFormatting {

    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("================================");
            while (scanner.hasNext()) {
                String text = scanner.next();
                int num = scanner.nextInt();
                System.out.printf("%-15s", text);
                System.out.printf("%03d%n", num);
            }
            System.out.println("================================");
        }
    }
}
