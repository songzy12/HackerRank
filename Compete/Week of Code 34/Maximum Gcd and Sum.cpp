#include <bits/stdc++.h>

using namespace std;

int maximumGcdAndSum(vector <int> A, vector <int> B) {
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
}
