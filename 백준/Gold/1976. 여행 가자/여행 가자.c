#include <stdio.h>
#define MAX_N 200
#define INF 10000000

int N, M;
int graph[MAX_N][MAX_N];
int plan[MAX_N];

void floyd_warshall() {
    for (int k = 0; k < N; k++) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (graph[i][k] + graph[k][j] < graph[i][j]) {
                    graph[i][j] = graph[i][k] + graph[k][j];
                }
            }
        }
    }
}

int main() {
    scanf("%d", &N);
    scanf("%d", &M);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &graph[i][j]);
            if (i != j && graph[i][j] == 0) graph[i][j] = INF;
        }
    }
    for (int i = 0; i < M; i++) {
        scanf("%d", &plan[i]);
    }
    floyd_warshall();
    for (int i = 0; i < M - 1; i++) {
        if (graph[plan[i] - 1][plan[i + 1] - 1] == INF) {
            printf("NO\n");
            return 0;
        }
    }
    printf("YES\n");
    return 0;
}
