// I think it need to be solved by dp on prime factors

// no, 
// just for each possible gcd, 
// record its largest multiplier in A and B
// then iterate to find the right gcd

// n/1 + n/2 + ... + n/n = O(n \log n)

#include "bits/stdc++.h"
using namespace std;
const int N = 1e6 + 6;
int cnt[N];
int lmulA[N];
int lmulB[N];
int n;
int arr[N];
int brr[N];
int main() {
	scanf("%d" , &n);
	for(int i = 1; i <= n; ++i) {
		scanf("%d" , arr + i);
	}
	for(int i = 1; i <= n; ++i) {
		scanf("%d" , brr + i);
	}
	for(int i = 1; i <= n; ++i) {
		++cnt[arr[i]];
	}
	for(int i = 1; i < N; ++i) {
		for(int j = i; j < N; j += i) {
			if(cnt[j]) {
				lmulA[i] = max(lmulA[i] , j);
			}
		}
	}
	for(int i = 1; i <= n; ++i) {
		--cnt[arr[i]];
	}
	for(int i = 1; i <= n; ++i) {
		++cnt[brr[i]];
	}
	for(int i = 1; i < N; ++i) {
		for(int j = i; j < N; j += i) {
			if(cnt[j]) {
				lmulB[i] = max(lmulB[i] , j);
			}
		}
	}
	int mx = 0;
	for(int i = 1; i < N; ++i) {
		if(lmulA[i] && lmulB[i]) {
			mx = i;
		}
	}
	printf("%d\n" , lmulA[mx] + lmulB[mx]);
	return 0;
}

/*int maximumGcdAndSum(vector <int> A, vector <int> B) {
    // Complete this function
    int max = 1;
    int sum = 0;
    for (int i = 0; i < A.size(); ++i)
        for (int j = 0; j < B.size(); ++j) {
            int temp_gcd = __gcd(A[i], B[j]);
            int temp_sum = A[i]+B[j];
            if (temp_gcd < max)
                continue;
            if (temp_gcd > max) {
                max = temp_gcd;
                sum = temp_sum;
                continue;
            }
            if (temp_sum > sum) {
                max = temp_gcd;
                sum = temp_sum;
            }
        }
            
    return sum;
}

int main() {
    int n;
    cin >> n;
    vector<int> A(n);
    for(int A_i = 0; A_i < n; A_i++){
       cin >> A[A_i];
    }
    vector<int> B(n);
    for(int B_i = 0; B_i < n; B_i++){
       cin >> B[B_i];
    }
    int res = maximumGcdAndSum(A, B);
    cout << res << endl;
    return 0;
}*/