package HackerRank.projecteuler;

import java.util.Scanner;

public class euler026 {
    static int test(int limit) {
        int maxLength = 0;
        int result = 0;

        for (int d = 2; d < limit; d++) {
            int[] remainders = new int[d];
            int value = 1;
            int position = 0;

            while (remainders[value] == 0 && value != 0) {
                remainders[value] = position;
                value *= 10;
                value %= d;
                position++;
            }

            if (position - remainders[value] > maxLength) {
                maxLength = position - remainders[value];
                result = d;
            }
        }

        return result;
    }

    public static void main(String[] args) {
        try (Scanner in = new Scanner(System.in)) {
            int t = in.nextInt();
            for (int i = 0; i < t; i++) {
                int n = in.nextInt();
                System.out.println(test(n));
            }
        }
    }
}
