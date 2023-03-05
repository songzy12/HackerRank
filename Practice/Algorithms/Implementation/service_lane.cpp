#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
#include<cstring>
#include<map>
#include<iomanip>
#define DEBUG
using namespace std;
const int MAXN = 100000;
int width[MAXN], segTree[MAXN*3];
void build(int node, int begin, int end)    
{    
    if (begin == end)    
        segTree[node] = width[begin]; 
    else    
    {     
        build(2*node, begin, (begin+end)/2);
        build(2*node+1, (begin+end)/2+1, end);
		
        if (segTree[2 * node] <= segTree[2 * node + 1])    
            segTree[node] = segTree[2 * node]; 
        else    
            segTree[node] = segTree[2 * node + 1];
    }    
} 

int query(int node, int begin, int end, int left, int right)    
{   
	int p1, p2;    
	
	if (left > end || right < begin)    
		return -1;    
	
	if (begin >= left && end <= right)    
		return segTree[node];    
	
	p1 = query(2 * node, begin, (begin + end) / 2, left, right);   
	p2 = query(2 * node + 1, (begin + end) / 2 + 1, end, left, right);    
	
	if (p1 == -1)    
		return p2;    
	if (p2 == -1)    
		return p1;    
	if (p1 <= p2)    
		return  p1;    
	return  p2;      
}   

int main(){
#ifdef DEBUG
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	ios::sync_with_stdio(false);
	int N, T;
	cin>>N>>T;
	for(int i=0; i<N; ++i)
		cin>>width[i];
	build(1, 0, N-1);
	int i, j;
	while(T--){
		cin>>i>>j;
		cout<<query(1, 0, N-1, i, j)<<endl;
	}
	return 0;
}