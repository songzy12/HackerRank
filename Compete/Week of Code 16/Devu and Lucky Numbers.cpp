#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <queue>
#include <cstring>
#include <algorithm>
using namespace std;
const int Maxn = 340, Maxm = 32000 , Mo = 1e9 + 7;
#define ll long long 
int N , M , T;
int x , y , z;
ll C[Maxn][Maxn] ,pw[Maxn] , f[Maxn] , Revf[Maxn] , Rev9;
ll Pow(ll a, int b, int Mo){
    ll ans = 1;
    for (;b;b>>=1 , a = a * a % Mo)
        if (b & 1) ans = a * ans % Mo; // how to compute power
    return ans;
}
ll work(int x,int y,int z){  
    ll ans = (pw[x+y+z] - 1) * Rev9 % Mo;
    ans = ans * f[x+y+z-1] % Mo * Revf[x] % Mo * Revf[y] % Mo *Revf[z] % Mo;
    ans = ans * (4 * x + 5 * y + 6 * z) % Mo; // just a simple formula
    return ans;
}

int main() {
    // cin >> T;
    T =1;
    f[0] = Revf[0] = 1;
    for (int i=1;i<=301;i++) {
        f[i] = f[i-1] * i % Mo;
		// key: compute rev of factor
        Revf[i] = Revf[i-1] * Pow(i,Mo-2,Mo) % Mo; 
    }
    Rev9 = Pow(9,Mo-2,Mo);    
    pw[0] = 1;
    for (int i=1;i<=301;i++) pw[i] = pw[i-1] * 10 % Mo;
    while(T--){
        cin >> x >> y  >> z;
        ll ans = 0;
        for (int i=0;i<=x;i++)
            for (int j=0;j<=y;j++)
                for (int k=0;k<=z;k++)
                    if (i+j+k)
                        (ans += work(i,j,k))%=Mo;
        // cout << work(1,1,1) << endl;
        cout << (ans + Mo) % Mo << endl;
    }


    return 0;
}
