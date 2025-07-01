//openjdk version "23.0.1"

import java.util.Scanner;

public class practice {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int N = scan.nextInt();
		for(int i = 0; i < N; i++){
			String S = scan.next();
			System.out.println("Hello," +  S);
		}
		scan.close();
	}

}