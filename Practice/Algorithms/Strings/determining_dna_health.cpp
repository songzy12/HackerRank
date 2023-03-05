//satyaki3794
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <cassert>
#include <cstring>
#include <iomanip>
#define ff first
#define ss second
#define pb push_back
#define MOD (1000000007LL)
#define LEFT(n) (2*(n))
#define RIGHT(n) (2*(n)+1)

using namespace std;
typedef long long ll;
typedef pair<int, int> ii;
typedef pair<int, ii> iii;

ll pwr(ll base, ll p, ll mod = MOD){
    ll ans = 1;
    while(p){
        if(p&1)
            ans=(ans*base)%mod;
        base=(base*base)%mod;
        p/=2;
    }
    return ans;
}



const int N = 100002, MAXSIZE = 2000002;
int n, sz, trie[MAXSIZE][26], ends_here[MAXSIZE], sufflink[MAXSIZE];
char str[MAXSIZE];
int ticks, pattern_node[N], lo[MAXSIZE], hi[MAXSIZE];
vector<int> adj[MAXSIZE], query_nodes[N], subtract[N], add[N];
ll arr[N], ans[N];



void insert_pattern_string(int idx){

    int curr = 0;
    for(int i=0;str[i]!='\0';i++){
        int dir = str[i] - 'a';
        if(trie[curr][dir] == -1)
            trie[curr][dir] = ++sz;
        curr = trie[curr][dir];
    }
    pattern_node[idx] = curr;
}


void insert_query_string(int idx){

    int curr = 0;
    for(int i=0;str[i]!='\0';i++){
        int dir = str[i] - 'a';
        if(trie[curr][dir] == -1)
            trie[curr][dir] = ++sz;
        curr = trie[curr][dir];
        query_nodes[idx].pb(curr);
    }
}



void bfs(){

    sufflink[0] = 0;
    queue<int> qq;
    for(int i=0;i<26;i++)
        if(trie[0][i] != -1){
            sufflink[trie[0][i]] = 0;
            qq.push(trie[0][i]);
            adj[0].pb(trie[0][i]);
    // cout<<"added edge from 0 to "<<trie[0][i]<<endl;
        }

    while(!qq.empty()){

        int v = qq.front();
        qq.pop();
        for(int dir=0;dir<26;dir++){

            int vv = trie[v][dir];
            if(vv == -1)    continue;
            
            int j = sufflink[v];
            while(j > 0 && trie[j][dir] == -1)  j = sufflink[j];
            if(trie[j][dir] != -1)  sufflink[vv] = trie[j][dir];

            if(sufflink[vv] != vv){
                //create the new tree
                adj[sufflink[vv]].pb(vv);
            }
            qq.push(vv);
        }
    }
}


int next_state(int v, int dir){
    int j = v;
    while(j > 0 && trie[j][dir] == -1)  j = sufflink[j];
    if(trie[j][dir] != -1)  j = trie[j][dir];
    return j;
}


void dfs(int v) {
    lo[v] = ++ticks;
    for(int i=0;i<(int)adj[v].size();i++){
        dfs(adj[v][i]);
    }
    hi[v] = ticks;
}


ll BIT[MAXSIZE];

void update(int idx, ll val){
    // binary indexed tree
    while(idx <= ticks){
        BIT[idx] += val;
        idx += idx & (-idx);
    }
}

ll query(int idx){
    ll ans = 0;
    while(idx){
        ans += BIT[idx];
        idx -= idx & (-idx);
    }
    return ans;
}





int main(){

    // ios_base::sync_with_stdio(0);
    // cin.tie(0);

    scanf("%d", &n);
    sz = 0;
    memset(trie, -1, sizeof(trie));
    for(int i=1;i<=n;i++){
        scanf("%s", str);
        insert_pattern_string(i);
    }


    for(int i=1;i<=n;i++){
        scanf("%lld", &arr[i]);
    }

    int q;
    scanf("%d", &q);

    for(int i=1;i<=q;i++){
        int l, r;
        scanf("%d%d%s", &l, &r, str);
        l++;    r++;
        insert_query_string(i);
        subtract[l-1].pb(i);
        add[r].pb(i);
    }

    //create suffix links
    bfs();
    ticks = 0;
    //create the new tree
    dfs(0);

    for(int i=1;i<=n;i++){

        //"activate" this gene by executing range addition
        int node_in_trie = pattern_node[i];
        update(lo[node_in_trie], arr[i]);
        update(hi[node_in_trie]+1, -arr[i]);

        //subtract the value from all queries whose left endpoint is L+1
        for(auto it : subtract[i]){
            int idx = it;
            for(auto node_in_trie : query_nodes[idx])
                ans[idx] -= query(lo[node_in_trie]);
        }


        //add the value to all queries whose right endpoint is R
        for(auto it : add[i]){
            int idx = it;
            for(auto node_in_trie : query_nodes[idx])
                ans[idx] += query(lo[node_in_trie]);
        }
    }

    cout<<*min_element(ans+1, ans+q+1)<<" "<<*max_element(ans+1, ans+q+1);
    return 0;
}

// Let F(i, str) be the purity value of the string str when considering only the genes in the range 1 to i (inclusive). Then the answer for the query (L, R, str) is equal to the value F(R, str) - F(L-1, str).