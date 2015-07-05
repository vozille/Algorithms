/*
She's just like the first rays of sunshine,
after a stormy night.
*/

 // find depth of node using bfs

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int MOD = 1e9+7;
const double ESP = 1e-9;

vector< vector <int> > >graph;
bool visited[100005];
vector <int> depth;

void bfs(int n)
{
    depth[n] = 0;
    visited[n] = 1;
    queue<int> q;
    q.push(n);
    while(not q.empty())
    {
        int x = q.front();
        q.pop();
        for(auto i : graph[x])
        {
            if(not visited[i])
            {
                depth[i] = depth[x]+1;
                visited[i] = true;
                q.push(i);
            }
        }
    }
}
int main(void)
{
    freopen("input.txt","r",stdin);
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int n,i,j;
    cin >> n;

    cout << ans << '\n';
    return 0;
}
