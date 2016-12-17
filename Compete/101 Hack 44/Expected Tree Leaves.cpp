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


int main(){
    int n;
    cin >> n;
    return 0;
}

/*
    Given the number of vertices in the tree, help Anna by finding the expected number, $E$, of leaves in the tree. Then print the value of $E\times n! mod (1e9+7)$ as your answer.

    P_i = (i-1)/i \times i/(i+1) \times \dots (n-2)/(n-1) = (i-1) / (n-1)
    E = P_2 + P_3 + \dots + P_n = n / 2.
    So just print n / 2 \times n! mod (1e+7)
 */
