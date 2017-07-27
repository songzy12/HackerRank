nclude <cstdio>
#include <iostream>
#include <ctime>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <set>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <bitset>
#include <fstream>
#include <deque>
#include <stack>
#include <climits>
#include <string>
#include <queue>
#include <memory.h>
#include <map>
#include <unordered_map>

#define ll long long
#define ld double
#define pii pair <int, int>
#define pll pair <ll, ll>
#define mp make_pair

using namespace std;

const int maxn = (int)2e5 + 10;
vector <int> ed[maxn];
const int mod = (int)1e9 + 7;

// the key is to map f() to matrix multiplication
// thus convert f(m+n) to f(m)*f(n)
// here f(n) is the first element of M^n

struct mat {
	int a[2][2];

	mat() {
		memset(a, 0, sizeof a);
	}
};

mat operator *(mat x, mat y) {
	mat z;

	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < 2; j++) {
			for (int k = 0; k < 2; k++) {
				z.a[i][j] = (z.a[i][j] + (ll)x.a[i][k] * y.a[k][j]) % mod;
			}
		}
	}

	return z;
}

mat operator +(mat x, mat y) {
	mat z;

	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < 2; j++) {
			z.a[i][j] = x.a[i][j] + y.a[i][j];
			if (z.a[i][j] >= mod) {
				z.a[i][j] -= mod;
			}
		}
	}

	return z;
}

mat e;
mat f;

mat my_pow(mat a, int x) {
	if (x == 0) {
		return e;
	}

	if (x & 1) {
		return a * my_pow(a, x - 1);
	}

	mat g = my_pow(a, x >> 1);

	return g * g;
}

int d[maxn];
mat ans;

mat dfs(int v, int p = -1) {
	mat g = my_pow(f, d[v]); // g = f ^ {d[v]}
	mat sum = e;
	mat res = e;

	for (int i = 0; i < (int)ed[v].size(); i++) {
		int u = ed[v][i];

		if (u != p) {
			mat now = dfs(u, v); // now is sum of sons

			res = res + sum * now;
			sum = sum + now; 
		}
	}

	sum = sum * g;
	ans = ans + res * g;

	return sum;
}


int main() {
	e.a[0][0] = e.a[1][1] = 1;
	e.a[0][1] = e.a[1][0] = 0;
	f.a[0][0] = f.a[0][1] = f.a[1][0] = 1;
	f.a[1][1] = 0;

	int n;

	cin >> n;

	for (int i = 0; i < n - 1; i++) {
		int x, y;

		scanf("%d %d", &x, &y);

		ed[x].push_back(y);
		ed[y].push_back(x);
	}

	for (int i = 1; i <= n; i++) {
		scanf("%d", &d[i]);
	}

	dfs(1);
	
	int answer = ans.a[0][0] * 2;
	
	if (answer >= mod) {
	    answer -= mod;
	}
	
	for (int i = 1; i <= n; i++) {
	    answer -= my_pow(f, d[i]).a[0][0];
	    if (answer < 0) {
	        answer += mod;
	    }
	}

	cout << answer << endl;

	return 0;
}