#define REP(i, n) for(int i = 0; i < (int)(n); i++)
#include <stdio.h>

double DP[302][302][302];
double Nd = 0.0;

double solve(int i, int j, int k) {
	if (DP[i][j][k] >= 0.0) return DP[i][j][k];
	if (i+j+k == 0) return 0.0;
	double res = 0.0;
	if (i > 0) res += solve(i-1, j, k) * i;
	if (j > 0) res += solve(i+1, j-1, k) * j;
	if (k > 0) res += solve(i, j+1, k-1) * k;
	res += Nd;
	res /= (double)(i+j+k);
	DP[i][j][k] = res;
	return res;
}

int main() {
	int N = 0, d1 = 0, d2 = 0, d3 = 0, num;
	scanf("%d", &N);
	Nd = (double)N;
	double cnt = 1.0, mean = 0.0, N_inv;

	REP(i, N) {
		scanf("%d", &num);
		if (num == 1) d1++;
		if (num == 2) d2++;
		if (num == 3) d3++;
	}
	REP(i, N+2) REP(j, N+2) REP(k, N+2) DP[i][j][k] = -1.0;

	printf("%.12lf\n", solve(d1,d2,d3));
	return 0;
}
