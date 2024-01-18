package HackerRank.projecteuler;

import java.util.*;


//How many routes are there through a NxM grid from top to bottom? As number of ways can be very large, print it modulo (10^9+7).
public class euler015 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        
        for (int t = 0; t < T; t++) {
            int N = scanner.nextInt();
            int M = scanner.nextInt();
            long result = calculateRoutes(N, M);
            System.out.println(result);
        }
        
        scanner.close();
    }

    private static long calculateRoutes(int N, int M) {
        int MOD = 1000000007;
        long[][] dp = new long[N + 1][M + 1];
        
        for (int i = 0; i <= N; i++) {
            for (int j = 0; j <= M; j++) {
                if (i == 0 || j == 0) {
                    dp[i][j] = 1;
                } else {
                    dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD;
                }
            }
        }
        
        return dp[N][M];
    }
}
