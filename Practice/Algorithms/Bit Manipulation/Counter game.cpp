#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int T;
    cin>>T;
    while (T--) {
        unsigned long long N;
        cin>>N;
        int count = 0;
        while ((N & 0x1) == 0) {
            count ++;
            N >>= 1;
        }
        N >>= 1;
        while (N) {
            if ((N & 0x1L) == 1)
                count ++;
            N >>= 1;
        }
        cout<<(count % 2 ? "Louise" : "Richard")<<endl;
    }
    return 0;
}

// n &= n-1, set the last 1 bit to 0
// unsigned long long for N = 2^64-1
