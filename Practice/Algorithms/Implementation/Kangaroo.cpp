#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

int can(int x1, int v1, int x2, int v2) {
    if (v1 == v2)
        return x1 == x2;
    if ((x1 - x2) * (v2 - v1) < 0)
        return false;
    return (x1 - x2) % (v2 - v1) == 0;
}

int main(){
    int x1;
    int v1;
    int x2;
    int v2;
    cin >> x1 >> v1 >> x2 >> v2;
    cout << (can(x1, v1, x2, v2) ? "YES" : "NO") <<endl;
 
    return 0;
}

/* v1 may equal to v2
 * that makes (x1 - x2) % (v2 - v1) fail
 */