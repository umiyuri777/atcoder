package ABC360;
import java.util.Scanner;

public class B {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        String S = scan.next();
        String T = scan.next();

        for (int w = 1; w < S.length(); w++){
            for (int c = 0; c < w; c++){
                String now = "";
                for (int i = c; i < S.length(); i += w){
                    now += S.charAt(i);
                }
                if (now.equals(T)){
                    System.out.println("Yes");
                    scan.close();
                    return;
                }
            }
        }
        System.out.println("No");
        scan.close();
    }
}
