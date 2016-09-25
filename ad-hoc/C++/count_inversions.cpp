#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

typedef long long llong;

const int MAXN = 500020;

// binary indexed trees
llong tree[MAXN], A[MAXN], B[MAXN];
// find sum upto idx
llong read(int idx) {
	llong sum = 0;
	while (idx > 0) {
		sum += tree[idx];
		idx -= (idx & -idx);
	}
	return sum;
}
// update binary indexed trees
void update(int idx, llong val) {
	while (idx <= MAXN) {
		tree[idx] += val;
		idx += (idx & -idx);
	}
}

int main(void) {

	int N;
	// N is size of array
	// Enter the array
	scanf("%d", &N);
	memset(tree, 0, sizeof(tree));

	for (int i = 0; i < N; ++i) {
		scanf("%lld", &A[i]);
		B[i] = A[i];
	}

	sort(B, B + N);
	// inversion counted by comparing it to the sorted elements
	for (int i = 0; i < N; ++i) {
		int rank = int(lower_bound(B, B + N, A[i]) - B);
		A[i] = rank + 1;
	}
	for(int i = 0; i < N; i++){
		cout << A[i] << " ";
	}
	// counts number of inversion
	int inv_count = 0;
	for (int i = N - 1; i >= 0; --i) {
		int x = read(A[i] - 1);
		inv_count += x;
		update(A[i], 1);
	}
	printf("%d\n", inv_count);
	return 0;
}
