package HackerRank.projecteuler;

import java.util.*;


//What is the Nth prime number?
public class euler007 {

    public static void main(String[] args) {
        try (Scanner in = new Scanner(System.in)) {
            int t = in.nextInt();
            for (int a0 = 0; a0 < t; a0++) {
                int n = in.nextInt();
                int result = findNthPrime(n);
                System.out.println(result);
            }
        }
    }

    private static int findNthPrime(int n) {
        if (n == 1) {
            return 2;
        }

        List<Integer> primes = new ArrayList<>();
        primes.add(2);
        int num = 3;

        while (primes.size() < n) {
            if (isPrime(num, primes)) {
                primes.add(num);
            }
            num += 2;
        }

        return primes.get(n - 1);
    }

    private static boolean isPrime(int num, List<Integer> primes) {
        for (int prime : primes) {
            if (prime * prime > num) {
                break;
            }
            if (num % prime == 0) {
                return false;
            }
        }
        return true;
    }
}

