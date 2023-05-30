#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

int main()
{
#ifndef ONLINE_JUDGE
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	int N, Q;
	cin >> N >> Q;
	// vector<vector<int> > seqList(N, vector<int>());
	vector<vector<int>> seqList;
	for (int n = 0; n < N; ++n)
		seqList.push_back(vector<int>());
	int lastAns = 0;
	while (Q--)
	{
		int op, x, y;
		cin >> op >> x >> y;
		vector<int> &seq = seqList[(x ^ lastAns) % N]; // notice the `&`
		if (op == 1)
		{
			// seqList[(x ^ lastAns) % N].push_back(y);
			seq.push_back(y);
		}
		else
		{
			lastAns = seq[y % seq.size()];
			cout << lastAns << endl;
		}
	}
	return 0;
}