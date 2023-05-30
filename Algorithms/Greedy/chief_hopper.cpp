#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;

const int maxn = 1e5;
int h[maxn];
int N;

bool check(int energy, int max_ele)
{
    for (int i = 0; i < N; ++i)
    {
        if (energy < 0)
            return false;
        if (energy >= max_ele)
            return true;
        if (h[i] > energy)
            energy -= (h[i] - energy);
        else
            energy += (energy - h[i]); // energy may overflow, exponentially
    }
    return energy >= 0; // rather than return true
}

int main()
{

    // freopen("in.txt", "r", stdin);
    // freopen("out.txt", "w", stdout);

    cin >> N;
    for (int i = 0; i < N; ++i)
        cin >> h[i];
    int max_ele = *max_element(h, h + N);
    int l = 0, r = max_ele;
    if (check(l, max_ele))
    {
        cout << 0 << endl;
        return 0;
    }
    while (l < r)
    {
        int m = (l + r) / 2;
        if (check(m, max_ele))
        {
            r = m;
        }
        else
        {
            l = m + 1;
        }
    }
    cout << l << endl;
    return 0;
}

/* wrong answer: return energy >= 0;
   overflow: if (energy >= max_ele) return true;
 */