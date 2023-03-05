import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

	public static int[] generate(int x, int y) {
		return new int[] { x, 15 - x - y, y, 5 + y - x, 5, 5 + x - y, 10 - y, x + y - 5, 10 - x };
	}

	public static boolean check(int[] nums) {
		boolean[] flag = new boolean[10];
		for (int num : nums) {
			if (num < 1 || num > 9)
				return false;
			if (!flag[num])
				flag[num] = true;
			else
				return false;
		}
		return true;
	}

	public static ArrayList<int[]> valid_nums() {
		ArrayList<int[]> ans = new ArrayList<int[]>();
		for (int i = 1; i <= 9; ++i) {
			for (int j = 1; j <= 9; ++j) {
				int[] temp = generate(i, j);
				if (check(temp)) {
					ans.add(temp);
				}
			}
		}
		return ans;
	}

	public static int compute_cost(int[] s, int[] t) {
		int ans = 0;
		for (int i = 0; i < 9; ++i)
			ans += Math.abs(s[i] - t[i]);
		return ans;
	}

	public static int compute(int[][] s) {
		int cost = 81;
		ArrayList<int[]> nums = valid_nums();
		int[] t = new int[9];
		for (int i = 0; i < 3; ++i)
			for (int j = 0; j < 3; ++j)
				t[i * 3 + j] = s[i][j];
		for (int i = 0; i < nums.size(); ++i) {
			int temp = compute_cost(nums.get(i), t);
			if (temp < cost)
				cost = temp;
		}
		return cost;
	}

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int[][] s = new int[3][3];
		for (int s_i = 0; s_i < 3; s_i++) {
			for (int s_j = 0; s_j < 3; s_j++) {
				s[s_i][s_j] = in.nextInt();
			}
		}
		System.out.println(compute(s));
		// Print the minimum cost of converting 's' into a magic square
	}
}
