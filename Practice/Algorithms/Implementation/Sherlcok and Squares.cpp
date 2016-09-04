#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

const int N = sqrt(1e9)+1; // notice the scope
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
    int squre[N];
    for(int i=0; i<N; ++i){
        squre[i] = (i+1)*(i+1);
	}
    int T;
    cin>>T;
    while(T--){
        int A, B;
        cin>>A>>B;
        cout<<upper_bound(squre, squre+N, B)-lower_bound(squre, squre+N, A)<<endl;
    }
    return 0;
}
