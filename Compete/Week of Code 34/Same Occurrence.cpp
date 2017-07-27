#include<bits/stdc++.h>
#define fi first
#define se second
#define av ios_base::sync_with_stdio(0);cin.tie(0)
#define pb push_back
using namespace std;
int i,j,k,n,m,ar[8002],x,y,q,x2;
vector<int>adj[8002];
int dp[8002][8002];
int main()
{
    av;
    cin>>n>>q;

    // dp is only used for repeated query
    for(i=0; i<=(n+1); i++)
        for(j=0; j<=(n+1); j++)
            dp[i][j]=-1;
    
    // compressing
    int cnt=1;    
    unordered_map<int,int>mapp;
    for(i=0; i<n; i++) {
        cin>>ar[i];
        if(mapp[ar[i]]==0)
            mapp[ar[i]]=cnt++;
    }
    
    for(i=0; i<n; i++) {
        adj[mapp[ar[i]]].pb(i);
    }
    vector<pair<int,int> >temp;
    unordered_map<int,int>diff;
    int a1,a2;
    while(q--) {
    	cin>>x>>y;
        a1=mapp[x];
        a2=mapp[y];
        temp.clear();
        i=0;
        j=0;
        x=a1;
        y=a2;
        if(dp[x][y]!=-1) {
            cout<<dp[x][y]<<endl;
            continue;
        }
        if(x == y) {
            dp[x][y]=(n*(n+1))/2;
            cout<<dp[x][y]<<endl;
            continue;
        }
        
        // merge the position of occurrences of x and y in sorted order efficiently
		while((i<adj[x].size()) && (j<adj[y].size())) {
			if(adj[x][i]<adj[y][j]){
            	temp.pb({adj[x][i],0});
                i++;
            }
            else {
                temp.pb({adj[y][j],1});
                j++;
            }
        }
        while(i<adj[x].size()) {
			temp.pb({adj[x][i],0});
            i++;
        }
        while(j<adj[y].size()) {
       		temp.pb({adj[y][j],1});
            j++;
        }
        
        // If at the (i)th index of this merged vector if the position of occurrence(of x or y) be l and 
        // if at the (i+1)th index of this merged vector if the position of occurrence(of x or y) be r, 
        // then the number of times that the difference a - b occurs is r - l
        int cx = 0,cy = 0;
        diff.clear();
        int an = temp.size();
        diff[0] = 1; // since \binom{n}{2} + n = \binom{n+1}{2}
        if(an >= 1)
            diff[0]+=temp[0].fi;
        int cnt1 = 0,cnt2 = 0;
        an--;
        for(i=0; i<(an); i++) {
            if(temp[i].se == 0)
                cx++;
            if(temp[i].se == 1)
                cy++;
            diff[cx-cy]+=(temp[i+1].fi - temp[i].fi);
        }
        if(an+1 >= 1 && i >= 0 && i<n) {
            if(temp[i].se == 0)
                cx++;
            if(temp[i].se == 1)
                cy++;
            diff[cx-cy]+=(n - temp[i].fi);
        }
        
        int ans = 0;
        for(auto x:diff) {
            x2 = x.se;
            ans+=(((x2*(x2-1)))/2);
        }
        dp[a1][a2] = ans;
        cout<<dp[a1][a2]<<endl;
    }
    return 0;
}