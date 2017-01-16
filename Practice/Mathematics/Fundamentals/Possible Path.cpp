/* Adam正站在一个无限大的二维网格的(a,b)点。他想知道他能否到达(x,y)点。他唯一可做的操作是从某个点 (a,b)，移动到(a+b,b), (a,a+b), (a-b,b), 或者 (a,a-b) 。 他允许到二维网格的任何点，点的 X(或者 Y)坐标可以为正、负，0。
 *
 * 告诉Adam它能否到达(x,y)点
 */

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int t;
    cin>>t;
    while (t--) {
        int x, y, w, z;
        cin>>x>>y>>w>>z;
        cout<<(__gcd(x,y) == __gcd(w,z) ? "YES" : "NO")<<endl;
    }
    return 0;
}

/* Just check whether gcd(x, y) == gcd(z, w).
 * consider the execution of Eclidean Algorithm.
 * (x, y) -> (d, 0) -> (z, w)
 */