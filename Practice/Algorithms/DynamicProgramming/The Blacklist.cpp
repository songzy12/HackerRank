/* The gangster can use any number of these mercenaries. But he has to honor one condition set by them:
 * they have to be assigned in such a way that they eliminate a consecutive group of gangsters in the list
 */

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

const int maxn = 20;
const int maxk = 10;
int cost[maxk][maxn];

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n, k;
    cin>>n>>k;
    for (int i = 0; i < k; ++i)
        for (int j = 0; j < n; ++j)
            cin>>cost[i][j];
    // select zero or one consecutive section from each line.
    return 0;
}

/* dynamic programming over subsets using bitmasks
 */