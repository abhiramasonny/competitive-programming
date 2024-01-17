package HackerRank.projecteuler;
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;


//By considering the terms in the Fibonacci sequence whose values do not exceed N, find the sum of the even-valued terms.
public class euler002 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int a0 = 0; a0 < t; a0++){
            long n = in.nextLong();
            long sum = calculateEvenFibonacciSum(n);
            System.out.println(sum);
        }
    }

    private static long calculateEvenFibonacciSum(long n) {
        long sum = 0;
        long prev = 1;
        long current = 1;

        while (current <= n) {
            if (current % 2 == 0) {
                sum += current;
            }

            long next = prev + current;
            prev = current;
            current = next;
        }

        return sum;
    }
}
