#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <cstdlib>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
/* Head ends here */

bool isUniform(char a[], int len){
	int t = a[0];
	for(int i = 1; i < len; ++i)
		if(a[i] != t)
			return false;
	return true;
}

int count(char a[], int len, char c){
	int res = 0;
	for(int i=0; i<len; ++i)
		if(a[i] == c)
			res ++;
	return res;
}

int stringReduction(char a[]) {
    int len = strlen(a);
	if(isUniform(a, len))
		return len;
	else{
		int num_a = count(a, len, 'a');
		int num_b = count(a, len, 'b');
		int num_c = count(a, len, 'c');
		if(num_a % 2 && num_b % 2 && num_c % 2 ||
		!(num_a % 2) && !(num_b % 2) && !(num_c % 2))
		// aa, [2, 0, 0]
			return 2;
		else
			return 1;
	}
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
    int res, t, i;
    scanf("%d",&t);
    char a[100001];
    for (i=0;i<t;i++) {
        scanf("%s",a);
        res=stringReduction(a);
        printf("%d\n",res);  
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}
