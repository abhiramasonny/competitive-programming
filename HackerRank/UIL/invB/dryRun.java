import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class dryRun {

    public static void main(String[] args) {
        Scanner file = new Scanner(System.in);
        int t = file.nextInt();
        for(int i = 0; i<t; i++){
            System.out.println("I like "+ file.next() + ".");
        }
    }
}