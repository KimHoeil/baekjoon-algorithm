// 다익스트라 알고리즘. 
// 프림알고리즘이랑 매우 비슷함

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <climits>
#define MAX_SIZE 300001

using namespace std;

const long long INF = 1e18; // long형에서 나올 수 있는 매우 큰 값

struct edge {
    int end;
    int cost;

    // 최소힙
    bool operator<(const edge& b) const {
        return cost > b.cost;
    }
};

// cost가 포함된 인접리스트 (pair를 쓰셔도 됩니다)
// pair를 쓰다면 위처럼 연산자 오버로딩 안해도 됩니다.
vector<vector<edge>> adj(20001);
int dist[MAX_SIZE];

void djik(int n, int startNode) {
    priority_queue<edge> pq;

    // 초기화
    // 우선 모든 정점의 최단거리를 무한대로 숫자를 정해둔다
    for (int i = 0; i <= n; i++) {
        dist[i] = INT_MAX;
    }

    // 시작점을 큐에 넣고, dist를 0으로 설정한다
    pq.push({ startNode, 0 });
    dist[startNode] = 0;

    // 우선순위 큐에서 값을 꺼내온다
    while (!pq.empty()) {
        edge top = pq.top();
        pq.pop();

        int nowVertex = top.end;
        int nowCost = top.cost;

        // 해당 정점에서 나가는 간선들을 전체 순회하여, 다음 갈 수 있는 정점들에 대해 최단거리를 계산한다
        int len = adj[nowVertex].size();
        for (int i = 0; i < len; i++) {
            edge next = adj[nowVertex][i];

            // 다음에 갈 점의 최단거리보다, 지금 점 + 다음 점으로의 가중치가 더 작다면
            // 최단거리를 갱신하고, 큐에 해당 지점을 넣는다
            if (dist[next.end] > dist[nowVertex] + next.cost) {
                dist[next.end] = dist[nowVertex] + next.cost;
                pq.push({ next.end, dist[next.end] });    // 다음에 갈 지점을 큐에 넣어야함! 최단거리는 방금 계산한 그 값으로 넣어야함
            }
        }
    }
}

int main()
{
    int V, e, k;

    cin >> V >> e;
    cin >> k;

    // 그래프 초기화하기)
    for (int i = 1; i <= e; i++)
    {
        int u, v, w;
        cin >> u >> v >> w;

        adj[u].push_back({ v,w });

    }

    djik(V, k);

    for (int i = 1; i <= V; i++)
    {   
        if (dist[i] != INT_MAX)
            cout << dist[i] << '\n';
        else
            cout << "INF\n";
    }

    /*
    // 그래프 출력하기
    for (int i = 1; i <= V; i++) {
        if (adj[i].size() != 0)
        {
            for (int j = 0; j <= adj[i].size() - 1; j++)
            {
                cout << adj[i][j].end << ' ' << adj[i][j].cost << '\n';
            }
        }
    }
    */

    return 0;
}
