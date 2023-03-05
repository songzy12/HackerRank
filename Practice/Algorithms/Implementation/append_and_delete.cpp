#include <cmath>
#include <cstdio>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int compute(string s, string t)
{
    int i = 0;
    while (i < s.size() && i < t.size() && s[i] == t[i])
        i++;
    return s.size() + t.size() - 2 * i; // 2*i not i
}

bool valid(int least, int k, string s, string t)
{
    if (least > k)
        return false;
    if ((least - k) % 2 == 0)
        return true;
    if (k >= s.size() + t.size())
        return true;
    return false;
}

int main()
{
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    string s, t;
    int k;
    cin >> s >> t >> k;
    int least = compute(s, t);
    cout << (valid(least, k, s, t) ? "Yes" : "No") << endl;
    system("pause");
    return 0;
}
