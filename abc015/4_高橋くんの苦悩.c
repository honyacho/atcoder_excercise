#include <stdio.h>

int map[10001][50][51];
int data[51][2];

int main() {
	for (int i = 0; i < 10001; i++) {
		for (int j = 0; j < 50; j++) {
			for (int k = 0; k < 51; k++) {
				map[i][j][k] = 0;
			}
		}
	}

	int width = 0, num_lines = 0, num_screen_shots = 0;
	scanf("%d", &width);
	scanf("%d %d", &num_lines, &num_screen_shots);

	for (int i = 0; i < num_lines; i++) {
		scanf("%d %d", &data[i][0], &data[i][1]);
	}

	for (int i = 0; i <= width; i++) {
		for (int j = 1; j <= num_screen_shots; j++) {
			for (int k = 1; k <= num_lines; k++) {
				int max1 = map[i][j][k - 1];
				int max2 = 0;
				if (i >= data[k-1][0]) max2 = map[i - data[k-1][0]][j-1][k-1] + data[k-1][1];
				if (max1 < max2) max1 = max2;
				map[i][j][k] = max1;
			}
		}
	}

	printf("%d\n", map[width][num_screen_shots][num_lines]);
}
