package HackerRank.projecteuler;

import java.util.Scanner;

public class euler009 {
    
    //find max pyth tripplet (a<b<c && a^2 + b^2 = c^2)
    public static void main(String[] args) {
        try (Scanner in = new Scanner(System.in)) {
            int t = in.nextInt();
            for(int a0 = 0; a0 < t; a0++){
                int n = in.nextInt();
                int result = findMaxPythagoreanTripletProduct(n);
                System.out.println(result);
            }
        }
    }

    private static int findMaxPythagoreanTripletProduct(int n) {
        int maxProduct = -1;
        for (int a = 1; a < n / 3; a++) {
            int b = (n * n - 2 * n * a) / (2 * (n - a));
            int c = n - a - b;
            if (a * a + b * b == c * c && a + b + c == n) {
                int product = a * b * c;
                maxProduct = Math.max(maxProduct, product);
            }
        }
        return maxProduct;
    }
}
