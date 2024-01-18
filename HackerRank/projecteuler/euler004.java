package HackerRank.projecteuler;

import java.util.Scanner;

//Find the largest palindrome made from the product of two 3-digit numbers which is less than N
public class euler004 {
    
    public static void main(String[] args) {
        try (Scanner in = new Scanner(System.in)) {
            int t = in.nextInt();
            for (int a0 = 0; a0 < t; a0++) {
                int n = in.nextInt();
                System.out.println(findLargestPalindrome(n));
            }
        }
    }

    private static int findLargestPalindrome(int n) {
        int maxPalindrome = 0;
        for (int i = 999; i >= 100; i--) {
            for (int j = i; j >= 100; j--) {
                int product = i * j;
                if (product < n && isPalindrome(product) && product > maxPalindrome) {
                    maxPalindrome = product;
                }
            }
        }
        return maxPalindrome;
    }

    private static boolean isPalindrome(int num) {
        String strNum = Integer.toString(num);
        String reverseStr = new StringBuilder(strNum).reverse().toString();
        return strNum.equals(reverseStr);
    }
}
