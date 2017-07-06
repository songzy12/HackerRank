import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.util.stream.Stream;

public class Solution {

	public static Integer[] unique(Integer[] scores) {
		ArrayList<Integer> ans = new ArrayList<Integer>();
		for (int score: scores) {
			if (ans.isEmpty() || score != ans.get(ans.size()-1))
				ans.add(score);
		}
		return ans.toArray(new Integer[ans.size()]);
	}
	
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        Integer[] scores = new Integer[n];
        for(int scores_i=0; scores_i < n; scores_i++){
            scores[scores_i] = in.nextInt();
        }
        scores = unique(scores);
        
        int m = in.nextInt();
        Integer[] alice = new Integer[m];
        for(int alice_i=0; alice_i < m; alice_i++){
            alice[alice_i] = in.nextInt();
            int index = Arrays.binarySearch(scores, alice[alice_i], Collections.reverseOrder());
            if (index >= 0) // >=
            	System.out.println(index+1);
            else
            	System.out.println(-index);
        }
        // your code goes here
    }
}
