import java.util.Scanner;
import java.lang.Math;
import java.util.stream.IntStream;

public class Solution {
    
     public static void main(String []args){
        Scanner scanner = new Scanner(System.in);
        // default vars
        // line 1 - init
        scanner.nextInt(); // always 0 so skip leaving
        int classStartTime = scanner.nextInt(); 
        int numOfRoutes = scanner.nextInt();
        // line 2 - walking between routes
        int[] walks = new int[numOfRoutes+1];
        for (int i = 0; i <= numOfRoutes;i++) {
            walks[i] = scanner.nextInt();
        }
        int totalWalks = IntStream.of(walks).sum();
        // line 3 - time taken riding bus
        int totalBusRide = 0;
        for (int i = 0; i < numOfRoutes;i++) {
            totalBusRide += scanner.nextInt();
        }
        // line 4 - bus intervals
        int timeWaited = 0;
        for (int i = 0; i < numOfRoutes;i++) {
            timeWaited += Math.abs(walks[i] - scanner.nextInt());
        }
        int totalTravelTime = totalWalks + totalBusRide + timeWaited;
        if (totalTravelTime > classStartTime) {
            System.out.print("no");
        } else {
            System.out.print("yes");
        }
     }
}