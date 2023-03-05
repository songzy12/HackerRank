#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

int main()
{
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    map<string, int> m;
    int N;
    cin >> N;
    while (N--)
    {
        string s;
        cin >> s;
        m[s]++;
    }
    int Q;
    cin >> Q;
    while (Q--)
    {
        string s;
        cin >> s;
        cout << m[s] << endl;
    }

    return 0;
}
