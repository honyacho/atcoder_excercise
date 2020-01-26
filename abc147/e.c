#include <stdio.h>
#include <stdlib.h>

int MP[81][81][16000];
int AS[81][81];
int BS[81][81];
int DS[81][81];

int main() {
  int i = 0, j = 0, H, W, d, k;
  scanf("%d %d", &H, &W);
  for (i = 0; i < H; i++) {
    for (j = 0; j < W; j++) {
      scanf("%d", &AS[i][j]);
    }
  }
  for (i = 0; i < H; i++) {
    for (j = 0; j < W; j++) {
      scanf("%d", &BS[i][j]);
    }
  }
  for (i = 0; i < H; i++) {
    for (j = 0; j < W; j++) {
      DS[i][j] = abs(AS[i][j]-BS[i][j]);
    }
  }

  MP[0][0][DS[0][0]] = 1;
  for (i = 0; i < H; i++) {
    for (j = 0; j < W; j++) {
      d = DS[i][j];
      for (k = 0; k < 16000-d; k++) {
        if (i > 0) {
          MP[i][j][abs(k-d)] = MP[i][j][abs(k-d)] || MP[i-1][j][k];
          MP[i][j][abs(k+d)] = MP[i][j][abs(k+d)] || MP[i-1][j][k];
        }
        if (j > 0) {
          MP[i][j][abs(k-d)] = MP[i][j][abs(k-d)] || MP[i][j-1][k];
          MP[i][j][abs(k+d)] = MP[i][j][abs(k+d)] || MP[i][j-1][k];
        }
      }
    }
  }
  for (i = 0; i < 16000; i++) {
    if (MP[H-1][W-1][i]) {
      printf("%d\n", i);
      return 0;
    }
  }
  return 0;
}
