#include <iostream>
#include <algorithm>
#include <queue>
#define MAX 52

using namespace std;

char arr[MAX][MAX];
int dis[MAX][MAX];
int dx[4] = {-1, 0, 1, 0}; // 상,우,하,좌
int dy[4] = {0, 1, 0, -1};
queue<pair<int, int>> waterQ;
queue<pair<int, int>> copyWaterQ;
queue<pair<int, int>> sQ;
queue<pair<int, int>> copy_sQ;
queue<pair<int, int>> emptyQ;
int r, c;

bool vaild(int x, int y){
    if (x >=1 && y >=1 && x <= r && y <= c) return true;
    else return false;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    bool check = false;
    cin >> r >> c;

    // 티떱숲 지도 초기화
    for (int i=1; i<=r; i++) {
        for (int j=1; j<=c; j++) {
            cin >> arr[i][j];

            if (arr[i][j] == '*')
                waterQ.push({i,j});
            else if (arr[i][j] == 'S')
                sQ.push({i,j});
        }
    }

    // cout << '\n';

    int cnt=1;

    while(true){

        // 고슴도치가 비버굴에 도착하는 경로
        while(!sQ.empty()){
            int cur_r = sQ.front().first;
            int cur_c = sQ.front().second;

            sQ.pop();

            if (arr[cur_r][cur_c] == '*') continue;
            else {
                for (int i=0; i<4; i++){
                    int nx = cur_r + dx[i];
                    int ny = cur_c + dy[i];

                    if (vaild(nx, ny) && arr[nx][ny] == '.'){
                        arr[nx][ny] = 'S';
                        dis[nx][ny] = dis[cur_r][cur_c] + 1;
                        copy_sQ.push({nx, ny});
                    }
                    else if (vaild(nx, ny) && arr[nx][ny] == 'D'){
                        check = true;
                        dis[nx][ny] = dis[cur_r][cur_c] + 1;
                        sQ = queue<pair<int, int>> ();
                        copy_sQ = queue<pair<int, int>> ();
                        break;
                    }
                }
            }
        } // sQ while문 종료
        // cout << "반복횟수: " << cnt << '\n';
        //     for (int i=1; i<=r; i++) {
        //         for (int j=1; j<=c; j++) {
        //             cout << arr[i][j];
        //         }
        //         cout << "\n";
        //     }
        //     cout << '\n';

        swap(sQ, copy_sQ);

        // 물이 상하좌우로 퍼지는 마법
        while(!waterQ.empty()){
            int cur_r = waterQ.front().first;
            int cur_c = waterQ.front().second;

            waterQ.pop();

            for(int i=0; i<4; i++){
                int nx = cur_r + dx[i];
                int ny = cur_c + dy[i];

                // 상하좌우에 물 범람하기
                if (vaild(nx, ny) && arr[nx][ny] == '.'){
                    arr[nx][ny] = '*';
                    copyWaterQ.push({nx, ny});
                }
                else if (vaild(nx, ny) && arr[nx][ny] == 'S'){
                    arr[nx][ny] = '*';
                    copyWaterQ.push({nx, ny});
                }
            }
        } // waterQ while문 종료
        
        swap(waterQ, copyWaterQ);

        // cout << "반복횟수: " << cnt << '\n';
        // for (int i=1; i<=r; i++) {
        //         for (int j=1; j<=c; j++) {
        //             cout << arr[i][j];
        //         }
        //         cout << "\n";
        // }
        // cout << '\n';
        cnt++;
        if (sQ.empty()) break;
    }

    if (check == false) cout << "KAKTUS\n";
    else {
        for (int i=1; i<=r; i++) {
            for (int j=1; j<=c; j++) {
                if (arr[i][j] == 'D'){
                    cout << dis[i][j] << '\n';
                }
            }
        }
    }

    return 0;
}