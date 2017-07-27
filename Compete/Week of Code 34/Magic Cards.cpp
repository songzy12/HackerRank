#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <algorithm>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <ctime>
#include <queue>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <cassert>
#include <unordered_map>
#include <bitset>
#include <unordered_set>

using namespace std;

#define pb push_back
#define pp pop_back
#define f first
#define s second
#define mp make_pair
#define sz(a) (int)((a).size())
#ifdef _WIN32
#  define I64 "%I64d"
#else
#  define I64 "%lld"
#endif
#define fname "."

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair < int, int > pi;

const int inf = (int)1e9 + 123;
const ll infl = (ll)1e18 + 123;
const double eps = 1e-10;

const int mod = (int)1e9 + 7;
const int MAX_N = (int)1e6 + 5;

int n, k, q;
vector < bool > cards[MAX_N], numbers[MAX_N];

ll ans[MAX_N][22];

ll val[1 << 20];
int used[1 << 20], timer, cnt;

int mask[MAX_N];

// key: when 2^n > m, the answer is simply \sum i^2.
// so we only treat the short queries beforehand

int main() {
#ifdef DEBUG
    freopen("input.txt", "r", stdin);
#endif
    scanf("%d%d%d", &n, &k, &q);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < k; j++)
            cards[i].pb(0);
    }
    for (int i = 0; i < k; i++) {
        for (int j = 0; j < n; j++)
            numbers[i].pb(0);
    }
    for (int i = 0, x, y; i < n; i++) {
        scanf("%d", &x);
        while(x--) {
            scanf("%d", &y);
            numbers[y - 1][i] = cards[i][y - 1] = 1;
        }
    }

    ll prod = 0;
    for (int i = 1; i <= k; i++) {
        prod += 1ll * i * i;
    }
    
    ll mini;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < k; j++)
            mask[j] = 0;
        for (int j = i; j < n && j - i + 1 <= 20; j++) {
            for (int id = 0; id < k; id++) {
                if (numbers[id][j])
                    mask[id] |= (1 << (j - i));
            }
            
            timer++;
            cnt = (1 << (j - i + 1));
            for (int id = 0; id < k; id++) {
                val[mask[id]] += 1ll * (id + 1) * (id + 1);
                if (used[mask[id]] != timer)
                    cnt--;
                used[mask[id]] = timer;
            }
            if (cnt > 0)
                ans[i][j - i + 1] = prod;
            else {
                mini = infl;
                for (int id = 0; id < k; id++)
                    mini = min(mini, val[mask[id]]);
                ans[i][j - i + 1] = prod - mini;
            }
            for (int id = 0; id < k; id++)
                val[mask[id]] = 0;
        }
    }
    for (int i = 1, l, r; i <= q; i++) {
        scanf("%d%d", &l, &r);
        l--, r--;
        if (r - l + 1 > 20) {
            printf("%lld\n", prod);
        } else {
            printf("%lld\n", ans[l][r - l + 1]);
        }
    }
    return 0;
}