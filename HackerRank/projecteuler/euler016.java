package HackerRank.projecteuler;

import java.math.BigInteger;
import java.util.Scanner;

public class euler016 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        
        for (int i = 0; i < T; i++) {
            int N = scanner.nextInt();
            BigInteger result = BigInteger.valueOf(2).pow(N);
            int sumOfDigits = calculateSumOfDigits(result);
            System.out.println(sumOfDigits);
        }
        
        scanner.close();
    }

    private static int calculateSumOfDigits(BigInteger number) {
        String numberString = number.toString();
        int sum = 0;
        
        for (int i = 0; i < numberString.length(); i++) {
            sum += Character.getNumericValue(numberString.charAt(i));
        }
        
        return sum;
    }
}
