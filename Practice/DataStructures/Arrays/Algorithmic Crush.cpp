#include <cmath>
#include <cstdio>
#include <cstring>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

// segment tree
// no need to use segment tree

const int MAXN = 1e7;
long long sum[MAXN+5];

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n, m;
    cin>>n>>m;
    memset(sum, 0, sizeof sum);
    while (m--) {
        int a, b;
        long long k; 
        cin>>a>>b>>k;
        sum[a] += k;
        if (b < n)
            sum[b + 1] -= k;
    }
    
    long long ans = 0;
    for (int i = 1; i <= n; ++i) {
        sum[i] += sum[i-1];
        if (sum[i] > ans)
            ans = sum[i];
    }
    cout<<ans<<endl;
    
    return 0;
}
