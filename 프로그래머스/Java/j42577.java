package Programmers;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class j42577 {

    public static void main(String[] args){
            String[] phone_book = {"119", "97674223", "1195524421"};
            System.out.println(solution(phone_book));

    }

    public static boolean solution(String[] phone_book) {

        boolean answer = true;

        Map<String, Integer> phone_book_map = new HashMap<String, Integer>();

        for(int a=0; a<phone_book.length; a++) {
            for(int b=1; b<phone_book[a].length(); b++) {
                phone_book_map.put(phone_book[a].substring(0,b),1);
            }
        }

        for(int a=0;a<phone_book.length;a++) {
            if(phone_book_map.containsKey(phone_book[a])){
                answer = false;
                break;
            }
        }

        return answer;
    }

}

