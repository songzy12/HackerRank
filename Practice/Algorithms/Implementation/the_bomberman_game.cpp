#include <iostream>
#include <cstdio>
using namespace std;

const int maxr = 200, maxc = 200;
char grid[maxr][maxc];
int state[maxr][maxc];

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int R, C, N;
    cin>>R>>C>>N;
    for (int i = 0; i < R; ++i)
        for (int j = 0; j < C; ++j) {
            cin>>grid[i][j];
            state[i][j] = grid[i][j] == 'O' ? 1 : -1; // order matters
        }
        
    
    for (int i = 0; i < R; ++i)
        for (int j = 0; j < C; ++j) 
            if (state[i][j] == 1) {
                int dx[] = {0, 0, -1, 1};
                int dy[] = {1, -1, 0, 0};
                for (int k = 0; k < 4; ++k) {
                    int ii = i + dx[k];
                    int jj = j + dy[k];
                    if (ii >= 0 && ii < R && jj >= 0 && jj < C
                        && state[ii][jj] != 1)
                        state[ii][jj] = 2;
                        // we use a different number to modify the state simultinously.
                }
            }
            
    // now -1 is all set 
    // then we set all 0
    
    for (int i = 0; i < R; ++i)
        for (int j = 0; j < C; ++j) 
            if (state[i][j] == -1) {
                int dx[] = {0, 0, -1, 1};
                int dy[] = {1, -1, 0, 0};
                for (int k = 0; k < 4; ++k) {
                    int ii = i + dx[k];
                    int jj = j + dy[k];
                    if (ii >= 0 && ii < R && jj >= 0 && jj < C
                        && state[ii][jj] != -1)
                        state[ii][jj] = 0;
                }
            }
    // not 1 || 2 should all be 1
    
    // 0: origin, 1: origin, 2: all, 3: -1, 4: all, 5: 1
    if (N == 1) {
        for (int i = 0; i < R; ++i) {
            for (int j = 0; j < C; ++j)
                cout<<grid[i][j];
            cout<<endl;
        }
    }
    else if (N % 4 == 0 || N % 4 == 2) {
        for (int i = 0; i < R; ++i) {
            for (int j = 0; j < C; ++j)
                cout<<'O';
            cout<<endl;
        }
    }    
    else if (N % 4 == 1) {
        for (int i = 0; i < R; ++i) {
            for (int j = 0; j < C; ++j)
                if (state[i][j] > 0)
                    cout<<'O';
                else 
                    cout<<'.';
            cout<<endl;
        }
    }
    else {
        for (int i = 0; i < R; ++i) {
            for (int j = 0; j < C; ++j)
                if (state[i][j] == -1)
                    cout<<'O';
                else 
                    cout<<'.';
            cout<<endl;
        }        
    }
    return 0;
}

/* the situation will loop
 * why second 1 is different from second 5?
 */
 
/* the reason is as follows:
 * set O as the original bombs, A is the grids that adjacent to O.
 * set L as the left grids (which is U - O - A)
 * set A' as the grids adjacent to L
 * then A \ne A'
 */
 
/* the first explosion will clear O + A
 * the second explosion will clear L + A'
 * while we set L' as U - L - A'
 * then A' is also adjacent to L'
 * afterwards the loop begins (between L + A' and L' + A')
 */