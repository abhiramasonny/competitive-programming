package HackerRank.projecteuler;

import java.math.BigInteger;
import java.util.Scanner;

//Work out the first ten digits of the sum of N 50 digit numbers.
public class euler013 {


    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        scanner.nextLine();
        
        BigInteger sum = BigInteger.ZERO;
        
        for (int i = 0; i < N; i++) {
            String numberStr = scanner.nextLine();
            BigInteger number = new BigInteger(numberStr);
            sum = sum.add(number);
        }
        
        String sumStr = sum.toString();
        if (sumStr.length() > 10) {
            System.out.println(sumStr.substring(0, 10));
        } else {
            System.out.println(sumStr);
        }
        
        scanner.close();
    }
}
