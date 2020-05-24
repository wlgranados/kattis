import java.util.Scanner;
import java.lang.Math;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numOfInputs = scanner.nextInt();
        double output = 0;
        for (int i = 0; i < numOfInputs;i++) {
            int initValue = scanner.nextInt();
            double powerOf = Math.pow(Math.floor(initValue / 10), initValue % 10);
            output += powerOf;
        }
        System.out.println((int) output);
    }
}