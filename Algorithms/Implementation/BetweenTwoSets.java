import java.util.*;

public class BetweenTwoSets {

	static int getGcd(int p, int q) {
		while (q != 0) {
			int temp = q;
			q = p % q;
			p = temp;
		}
		return p;
	}

	static int getGcd(int[] a) {
		int gcd = a[0];
		for (int i = 1; i < a.length; ++i)
			gcd = getGcd(gcd, a[i]);
		return gcd;
	}

	static int getLcm(int a, int b) {
		return a * b / getGcd(a, b);
	}

	static int getLcm(int[] a) {
		// here is how to compute lcm
		int ans = a[0];
		for (int i = 1; i < a.length; ++i) {
			ans = getLcm(ans, a[i]);
			if (ans > 100)
				return 101;
		}
		return ans;
	}

	static int getTotalX(int[] a, int[] b) {
		// Complete this function
		int lcm = getLcm(a);
		int gcd = getGcd(b);

		// System.out.println(lcm + " " + gcd);

		int ans = 0, i;
		for (i = 1; lcm * i <= gcd; ++i) {
			if (gcd % (lcm * i) == 0)
				ans++;
		}
		return ans;
	}

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		int m = in.nextInt();
		int[] a = new int[n];
		for (int a_i = 0; a_i < n; a_i++) {
			a[a_i] = in.nextInt();
		}
		int[] b = new int[m];
		for (int b_i = 0; b_i < m; b_i++) {
			b[b_i] = in.nextInt();
		}
		int total = getTotalX(a, b);
		System.out.println(total);
	}
}
