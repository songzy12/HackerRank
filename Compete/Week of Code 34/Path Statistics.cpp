// MO's algorithm

// there are at most \sqrt{N} distinct frequencies 

// DFS: start[u], end[u]
// a[start[u]] = a[end[u]] = u
// if u is ancestor of v, then [start[u], start[v]]
// if u is not ancestor of v, then [end[u], start[v]] + lowest_common_ancestor(u, v)

#include <bits/stdc++.h>

using namespace std;

constexpr int N = 50010, LN = 16;

vector<int> adj[N];

int depth[N], parent[LN][N]; // node depth and node parents sparse table
int ST[N], EN[N], cur_time = 0; // start and end time of sub-tree
int vec[2 * N]; // result of tree linearization
int val[N]; // node values

bool active[N]; // whether a node is active during mo's algorithm
int root[N];
int freq[N];
int ans[N];

void dfs(int u = 0, int d = 0, int prev = -1) {
    depth[u] = d;
    parent[0][u] = prev;

    ST[u] = cur_time++;
    vec[ST[u]] = u;

    for (int v : adj[u]) {
        if (v == prev) continue;
        dfs(v, d + 1, u);
    }

    EN[u] = cur_time++;
    vec[EN[u]] = u;
}

int lca(int u, int v) {
    if (depth[u] < depth[v]) swap(u, v);

    int diff = depth[u] - depth[v];
    for (int i = 0; i < LN; i++) {
        if ((diff >> i) & 1) {
            u = parent[i][u];
        }
    }

    if (u == v) return u;

    for (int i = LN - 1; i >= 0; i--) {
        if (parent[i][u] != parent[i][v]) {
            u = parent[i][u];
            v = parent[i][v];
        }
    }

    return parent[0][u];
}

constexpr int M = 320; // maximum number of distinct frequencies
constexpr int BS = 8; // bucket size (1 << BS)
constexpr int BC = (N >> BS) + 1; // bucket count

int t[M][BC << BS], bt[M][BC];
int quant[M]; // how many values are being stored at this frequency/bucket
int who[M]; // which frequency is being stored at this bucket

void add(int i, int p) {
    quant[i]++;
    t[i][p] = 1;
    bt[i][p >> BS]++;
}

void remove(int i, int p) {
    quant[i]--;
    t[i][p] = 0;
    bt[i][p >> BS]--;
}

int kquery(int i, int k) {
    int b = BC;
    while (b--) {
        if (k <= bt[i][b]) break;
        else k -= bt[i][b];
    }

    int p = (b + 1) << BS;
    while (p--) {
        if (k <= t[i][p]) break;
        else k -= t[i][p];
    }

    return p;
}

int qe[50000000], qh = 0, qt = 0;

void pre(int f) {
    if (root[f] == -1) {
        root[f] = qe[qh++];
        who[root[f]] = f;
    }
}

void pos(int f) {
    if (quant[root[f]] == 0) {
        who[root[f]] = -1;
        qe[qt++] = root[f];
        root[f] = -1;
    }
}

int main() {
    memset(parent, -1, sizeof parent);
    memset(root, -1, sizeof root);

    int n, q;
    scanf("%d %d", &n, &q);

    int S = sqrt(2 * n);

    vector<int> compr;
    for (int i = 0; i < n; i++) {
        scanf("%d", val + i);
        compr.push_back(val[i]);
    }

    sort(begin(compr), end(compr));
    compr.resize(unique(begin(compr), end(compr)) - begin(compr));

    for (int i = 0; i < n; i++) {
        val[i] = lower_bound(begin(compr), end(compr), val[i]) - begin(compr);
    }

    for (int i = 1; i < n; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        u--, v--;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dfs();

    for (int i = 1; i < LN; i++) {
        for (int j = 0; j < n; j++) {
            if (parent[i - 1][j] != -1) {
                parent[i][j] = parent[i - 1][parent[i - 1][j]];
            }
        }
    }

    using st = tuple<int, int, int, int, int>;
    vector<st> queries;

    for (int i = 0; i < q; i++) {
        int u, v, k;
        scanf("%d %d %d", &u, &v, &k);
        u--, v--;

        if (ST[u] > ST[v]) swap(u, v);

        int p = lca(u, v);
        if (p == u) queries.emplace_back(ST[u], ST[v], k, i, -1);
        else queries.emplace_back(EN[u], ST[v], k, i, p);
    }

    sort(begin(queries), end(queries), [&](const st& a, const st& b) -> bool {
        int l1, r1;
        int l2, r2;

        tie(l1, r1, ignore, ignore, ignore) = a;
        tie(l2, r2, ignore, ignore, ignore) = b;

        if (l1 / S != l2 / S) return l1 / S < l2 / S;
        return r1 < r2;
    });

    for (int i = 0; i < M; i++) {
        qe[qt++] = i;
    }

    auto insert = [&](int u) {      
        int v = val[u];
        active[u] = true;

        if (freq[v] != 0) {
            remove(root[freq[v]], v);
            pos(freq[v]);
        }

        freq[v]++;
        pre(freq[v]);
        add(root[freq[v]], v);
    };

    auto erase = [&](int u) {
        int v = val[u];
        active[u] = false;

        remove(root[freq[v]], v);
        pos(freq[v]);

        freq[v]--;

        if (freq[v] != 0) {
            pre(freq[v]);
            add(root[freq[v]], v);
        }
    };

    auto toggle = [&](int u) {
        if (active[u]) erase(u);
        else insert(u);
    };

    int L = 0, R = -1;
    for (auto& qry : queries) {
        int l, r, k, i, p;
        tie(l, r, k, i, p) = qry;

        while (R < r) toggle(vec[++R]);
        while (R > r) toggle(vec[R--]);
        while (L < l) toggle(vec[L++]);
        while (L > l) toggle(vec[--L]);

        if (p != -1) toggle(p);

        vector<int> freqs;
        for (int i = 0; i < M; i++) {
            if (who[i] != -1) {
                freqs.push_back(who[i]);
            }
        }

        sort(freqs.rbegin(), freqs.rend());

        for (auto f : freqs) {
            if (k <= quant[root[f]]) {
                ans[i] = compr[kquery(root[f], k)];
                break;
            } else {
                k -= quant[root[f]];
            }
        }

        if (p != -1) toggle(p);
    }

    for (int i = 0; i < q; i++) {
        printf("%d\n", ans[i]);
    }

    return 0;
}