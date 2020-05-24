import java.lang.Character;
import java.util.Scanner;

public class Solution{

     public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        String output = "";
        for (int i = 0; i < input.length(); i++){
            char c = input.charAt(i);        
            if (Character.isUpperCase(c)) {
                output += c;
            }
        }
        System.out.print(output);
     }
}