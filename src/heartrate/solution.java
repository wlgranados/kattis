import java.util.Scanner;
import java.util.Scanner;
import java.lang.Math;
import java.text.DecimalFormat;

public class Solution {
     public static void main(String[] args){
        DecimalFormat df = new DecimalFormat("#.####");
        Scanner scanner = new Scanner(System.in);
        int numOfInputs = scanner.nextInt();
        for (int i = 0; i < numOfInputs;i++) {
            int beats = scanner.nextInt();
            double seconds = scanner.nextDouble();
            double actualBPM = 60 / seconds;
            double calculatedBPM = (double) 60 * (beats) / seconds;
            double minBPM = calculatedBPM - actualBPM;
            double maxBPM = calculatedBPM + actualBPM;
            System.out.println(df.format(minBPM) + " " + df.format(calculatedBPM) + " " + df.format(maxBPM));
        }
     }
}