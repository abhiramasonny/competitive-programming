package HackerRank.projecteuler;

import java.util.*;

//What is the largest prime factor of a given number N?
public class euler003 {
    
    public static void main(String[] args) {
        try (Scanner in = new Scanner(System.in)) {
            int t = in.nextInt();
            for (int a0 = 0; a0 < t; a0++) {
                long n = in.nextLong();
                long largestPrimeFactor = getLargestPrimeFactor(n);
                System.out.println(largestPrimeFactor);
            }
        }
    }

    private static long getLargestPrimeFactor(long n) {
        long largestPrime = -1;

        while (n % 2 == 0) {
            largestPrime = 2;
            n /= 2;
        }

        for (long i = 3; i <= Math.sqrt(n); i += 2) {
            while (n % i == 0) {
                largestPrime = i;
                n /= i;
            }
        }

        if (n > 2) {
            largestPrime = n;
        }

        return largestPrime;
    }
}
