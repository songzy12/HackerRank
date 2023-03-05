// https://www.hackerrank.com/challenges/possible-path/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <numeric>
#include <algorithm>

int main()
{
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t;
    std::cin >> t;
    while (t--)
    {
        int x, y, w, z;
        std::cin >> x >> y >> w >> z;
        std::cout << (std::gcd(x, y) == std::gcd(w, z) ? "YES" : "NO") << std::endl;
    }
    return 0;
}

/* Just check whether gcd(x, y) == gcd(z, w).
 * consider the execution of Eclidean Algorithm.
 * (x, y) -> (d, 0) -> (z, w)
 */