#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
freopen("in.txt", "r", stdin);
freopen("out.txt", "w", stdout);   
	int T;
    cin>>T;
    while(T--){
        int n, a, b;
        cin>>n>>a>>b;
		if(a == b){
            cout<<(n-1)*a<<endl;
            continue;
        }
		if(a>b){ // ascending order
			int temp = a;
			a = b;
			b = temp;
		}
        for(int i=0; i<n; ++i)
            cout<<i*b+(n-1-i)*a<<" ";
        cout<<endl;
    }
    return 0;
}
