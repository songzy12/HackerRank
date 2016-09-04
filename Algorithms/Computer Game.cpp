#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
#define SZY
// TLE
int A[100000], B[100000];
vector<int> edgeA[100000], edgeB[100000];
int matchA[100000], matchB[100000];
bool visited[100000];
int res;

int path(int a){
	for(int i = 0; i < edgeA[a].size(); i++){
		int b = edgeA[a][i];
		if(visited[b])
			continue;
		visited[b] = true;
		if (matchB[b] == -1 || path(matchB[b])){
			matchA[a] = b;
			matchB[b] = a;
			return 1;
		}
	}
	return 0;
}

int main() {
#ifdef SZY
	freopen("in_.txt", "r", stdin);
	freopen("out_.txt", "w", stdout);
#endif
	int n;
	cin>>n;
	for(int i = 0; i < n; ++i)
		cin>>A[i];
	for(int i = 0; i < n; ++i)
		cin>>B[i];
	for(int i = 0; i < n; ++i)
		for(int j = 0; j < n; ++j)
			if(__gcd(A[i], B[j]) != 1){
				edgeA[i].push_back(j);
				edgeB[j].push_back(i);
			}
	memset(matchA, -1, sizeof matchA);
	memset(matchB, -1, sizeof matchB);
	for(int i = 0; i < n; i++){
		if(matchA[i] == -1){
			memset(visited, false, sizeof visited);
			res += path(i);
		}
	}
	cout<<res<<endl;
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
