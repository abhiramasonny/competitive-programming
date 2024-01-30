import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        long[] a = new long[n];

        for (int i = 0; i < n; i++) {
            a[i] = scanner.nextLong();
        }

        long ans = Long.MAX_VALUE;
        long sum = 0;

        for (int i = n - 1; i >= 0; i--) {
            sum += a[i];

            long target = 0;
            if (i > 0) {
                target = Math.max(0, target - sum);
            }

            ans = Math.min(ans, (long) Math.ceil((double) target / (n - i)));
        }

        System.out.println(ans);
    }
}
