package HackerRank.projecteuler;

import java.util.*;

//What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in a 20x20 grid?
public class euler011 {

    public static void main(String[] args) {
        try (Scanner in = new Scanner(System.in)) {
            int[][] grid = new int[20][20];
            
            for(int grid_i=0; grid_i < 20; grid_i++){
                for(int grid_j=0; grid_j < 20; grid_j++){
                    grid[grid_i][grid_j] = in.nextInt();
                }
            }
            
            int maxProduct = 0;
            
            for (int i = 0; i < 20; i++) {
                for (int j = 0; j < 17; j++) {
                    int product = grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3];
                    maxProduct = Math.max(maxProduct, product);
                }
            }
            for (int i = 0; i < 17; i++) {
                for (int j = 0; j < 20; j++) {
                    int product = grid[i][j] * grid[i + 1][j] * grid[i + 2][j] * grid[i + 3][j];
                    maxProduct = Math.max(maxProduct, product);
                }
            }
            for (int i = 0; i < 17; i++) { //woah pyth theorm
                for (int j = 0; j < 17; j++) {
                    int product = grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][j + 2] * grid[i + 3][j + 3];
                    maxProduct = Math.max(maxProduct, product);
                }
            }
            for (int i = 0; i < 17; i++) {
                for (int j = 3; j < 20; j++) {
                    int product = grid[i][j] * grid[i + 1][j - 1] * grid[i + 2][j - 2] * grid[i + 3][j - 3];
                    maxProduct = Math.max(maxProduct, product);
                }
            }
            System.out.println(maxProduct);
        }
     }
    

}
