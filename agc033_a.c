#include <stdio.h>

int queue[1000020][3];
char instr[1000][1001];
int checked[1000][1000];
int st = 0;
int en = 0;
int df[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

void append(int i, int j, int k) {
	queue[en][0] = i;
	queue[en][1] = j;
	queue[en][2] = k;
	checked[i][j] = 1;
	en++;
	return;
}

int main() {
	int H,W,res = 0;
	scanf("%d %d\n",&H,&W);
	for (int i=0;i<H;i++) gets(instr[i]);
	for (int i=0;i<H;i++) for (int j=0;j < W;j++) checked[i][j]=0;
	for (int i=0;i<H;i++) for (int j=0;j < W;j++) {
		if (instr[i][j] == '#') {
			checked[i][j]=1;
			queue[en][0]=i;
			queue[en][1]=j;
			queue[en][2]=0;
			en++;
		}
	}

	while (st < en) {
		int i = queue[st][0];
		int j = queue[st][1];
		int k = queue[st][2];
		st++;
		for (int l = 0; l < 4; l++) {
			if (i+df[l][0]<H && i+df[l][0]>=0 && j+df[l][1]<W && j+df[l][1] >= 0 && !checked[i+df[l][0]][j+df[l][1]]) {
				append(i+df[l][0], j+df[l][1], k+1);
				res = k+1;
			}
		}
	}
	printf("%d\n", res);
	return 0;
}
