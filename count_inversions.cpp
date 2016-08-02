#include <algorithm>
#include <cstdio>
#include <cstring>

using namespace std;

typedef long long llong;

const int MAXN = 500020;
llong tree[MAXN], A[MAXN], B[MAXN];

llong read(int idx) {
	llong sum = 0;
	while (idx > 0) {
		sum += tree[idx];
		idx -= (idx & -idx);
	}
	return sum;
}

void update(int idx, llong val) {
	while (idx <= MAXN) {
		tree[idx] += val;
		idx += (idx & -idx);
	}
}

int main(void) {
	freopen("input.txt", "r", stdin);
	int N,tc;
	scanf("%d", &tc);
	while (tc--) {
		scanf("%d", &N);
		memset(tree, 0, sizeof(tree));
		for (int i = 0; i < N; ++i) {
			scanf("%lld", &A[i]);
			B[i] = A[i];
		}
		sort(B, B + N);
		for (int i = 0; i < N; ++i) {
			int rank = int(lower_bound(B, B + N, A[i]) - B);
			A[i] = rank + 1;
		}
		int inv_count = 0;
		for (int i = N - 1; i >= 0; --i) {
			int x = read(A[i] - 1);
			if (x > 2){
				inv_count = -1;
				break;
			}
			inv_count += x;
			update(A[i], 1);
		}
		if(inv_count < 0)
			printf("%s\n", "Too chaotic");
		else
			printf("%lld\n", inv_count);
	}
	return 0;
}
