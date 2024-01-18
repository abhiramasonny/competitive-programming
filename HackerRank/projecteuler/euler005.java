package HackerRank.projecteuler;

import java.util.*;

//What is the smallest positive number that is evenly divisible(divisible with no remainder) by all of the numbers from 1 to N?
public class euler005 {
    public static void main(String[] args) {
        try (Scanner in = new Scanner(System.in)) {
            int t = in.nextInt();
            for(int a0 = 0; a0 < t; a0++){
                int n = in.nextInt();
                int result = findSmallestMultiple(n);
                System.out.println(result);
            }
        }
    }

    private static int findSmallestMultiple(int n) {
        int result = 1;
        for (int i = 2; i <= n; i++) {
            result = lcm(result, i);
        }
        return result;
    }

    private static int gcd(int a, int b) {
        while (b > 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    private static int lcm(int a, int b) {
        return a * (b / gcd(a, b));
    }
}
