import java.util.Scanner;

public class B {
    public static void main(String[] args) throws Exception {
        Scanner scan = new Scanner(System.in);
        String str1 = scan.next();
        
        int zero_count = 0;
        boolean zero_flag = false;
        int other_count = 0;
        
        for (int i = 0; i < str1.length(); i++){
            if (str1.charAt(i) == '0'){
                if(zero_flag == false){
                    zero_flag = true;
                }
                zero_count++;
            }
            else if (str1.charAt(i) != '0'){
                if (zero_flag == true){
                    other_count += zero_calculation(other_count, zero_count);
                    zero_count = 0;
                    zero_flag = false;
                }
                other_count += 1;
            }
            
        }
        other_count += zero_calculation(other_count, zero_count);
        System.out.println(other_count);
        scan.close();
    }
    
    static int zero_calculation(int other_count, int zero_count){
        if (zero_count % 2 == 0){
            return zero_count / 2;
        }
        else{
            return zero_count / 2 + 1;
        }
    }
}
