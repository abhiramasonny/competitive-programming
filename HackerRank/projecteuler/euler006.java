package HackerRank.projecteuler;

import java.util.*;

//Find the absolute difference between the sum of the squares of the first N natural numbers and the square of the sum.
public class euler006 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int a0 = 0; a0 < t; a0++){
            int n = in.nextInt();
            
            long sumOfSquares = 0;
            for (int i = 1; i <= n; i++) {
                sumOfSquares += i * i;
            }
            
            long sum = n * (n + 1) / 2;
            long squareOfSum = sum * sum;
            
            long absoluteDifference = Math.abs(sumOfSquares - squareOfSum);
            
            System.out.println(absoluteDifference);
        }
    }
}
