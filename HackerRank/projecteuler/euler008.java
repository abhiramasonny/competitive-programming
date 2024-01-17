package HackerRank.projecteuler;

import java.util.Scanner;

//Find the greatest product of K consecutive digits in the N digit number.
public class euler008 {
    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int a0 = 0; a0 < t; a0++){
            int n = in.nextInt();
            int k = in.nextInt();
            String num = in.next();
            
            long maxProduct = 0;
            
            for (int i = 0; i <= n - k; i++) {
                long product = 1;
                for (int j = 0; j < k; j++) {
                    product *= Character.getNumericValue(num.charAt(i + j));
                }
                if (product > maxProduct) {
                    maxProduct = product;
                }
            }
            
            System.out.println(maxProduct);
        }
    }
}
