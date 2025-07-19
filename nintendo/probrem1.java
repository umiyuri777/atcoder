/*
入力された文字列（コード）に対して、3桁の数字からなるIDを発行するプログラムを実装してください。

行ごとに、スペース区切りで複数の文字列（コード）が順番に入力されます。コードは大小英数字で構成されています。
入力されるコードに対して、それが 大文字・小文字を考慮せず その行で初めて入力されるコードの場合は、0埋めされた3桁の数字を 1 から順にIDとして払い出します。（例：001 002 003 ...）
その行の中ですでに同じコードが入力されている場合は、そのコードに対して過去に出力した最後のIDに 100 を足した数字をIDとして払い出します。（例：101 201 301 ...）
ただし、数字が4桁を超えてしまう場合には初めて入力されたコードとして新たに3桁の数字をIDとして払い出してください。
その行で発行されたIDを、発行された順にスペース区切りで出力してください。

行の中で、100種類以上のコードが入力されることはありません。
入力の先頭行には、その後に何行の問題が続くかが自然数で書いてあります。

入力例
3
aaa bbb ccc ddd eee
a a b a b c
aaa aaA aAA AAA aaa aaA aAA AAA aaa aaA aAA AAA

出力例
001 002 003 004 005
001 101 002 201 102 003
001 101 201 301 401 501 601 701 801 901 002 102

 */



// openjdk version "23.0.1"

import java.util.*;

public class probrem1 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        scan.nextLine();

        // 全ての行を受け取る
        String[] lines = new String[N];
        for (int i = 0; i < N; i++) {
            lines[i] = scan.nextLine();
        }

        // 各行処理
        for (String line: lines) {
            String[] words = line.split(" ");

            // 発見した文字列を記録しておくmapを定義
            Map<String, Integer> checked_stringMap = new HashMap<String, Integer>();
            
            String ans = "";

            // 発見した文字列の種類
            int word_kinds = 0;
            for (int column = 0; column < words.length; column++){
                String Lowered_word = words[column].toLowerCase();

                // 初めて入力された文字列の場合
                if (!checked_stringMap.containsKey(Lowered_word)){
                    checked_stringMap.put(Lowered_word, word_kinds + 1);
                    word_kinds++;
                    ans += String.format("%03d", checked_stringMap.size());
                }
                // すでに入力されたことがある文字列の場合
                else{
                    int newId = checked_stringMap.get(Lowered_word) + 100;

                    // 4桁を超えるときは初めて入力されたコードとして3桁のIDを払い出す
                    if (newId >= 1000){
                        newId = word_kinds + 1;
                        word_kinds++;
                    }
                    checked_stringMap.put(Lowered_word, newId);
                    ans += String.format("%03d", newId);
                }
                //　行の最後でなければ空白を挿入
                if (column != words.length - 1){
                    ans  += " ";
                }
            }
            System.out.println(ans.toString());
        }
        scan.close();
	}
}