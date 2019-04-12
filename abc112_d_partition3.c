#include <stdio.h>

int main(int argc, char** arcv) {
	int n = 0, m = 0, tmp = 0, res = 0;
	scanf("%d", &n);
	scanf("%d", &m);
	tmp= m / n;
	for (int i = tmp; 0 < i; i--) {
		if (!(m % i)) {
			printf("%d\n", i);
			return 0;
		}
	}
	return 0;
}
