/*
  find depth of node using bfs
  C++ 11 or higher
  This example uses BFS to find the depth of each node from the source
*/
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
                depth[i] = depth[x] + 1;
                visited[i] = true;
                q.push(i);
            }
        }
    }
}
/*
  To test:
  enter N , the number of edges
  enter all pairs U, V where each pair represents two vertices joined by edge
*/

int main(){
   int N;
   cin >> N;
   for(int i = 0; i < N; i++){
      int u, v;
      cin >> u >> v;
      graph[u].push_back(v);
      graph[v].push_back(u);
   }
   // use any vertex in graph as a source to pass to bfs()
}
