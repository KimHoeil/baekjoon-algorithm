#include <iostream>
#include <vector>

#define MAX 4
#define endl "\n"

using namespace std;

struct Fish
{
	int x;
	int y;
	int d;
	bool life;
};

int arr[MAX][MAX];
Fish fish[20];

int dx[] = {0,-1,-1,0,1,1,1,0,-1}; // 상,좌상,좌,좌하,하,우하,우,우상
int dy[] = {0,0,-1,-1,-1,0,1,1,1};

int ai, bi;
int Answer;

// 물고기 번호 합의 최대값 비교하는 함수
int Max(int A, int B) { if (A > B) return A; return B; }

bool Valid(int x, int y)
{
	if (x >= 0 && y >= 0 && x < 4 && y < 4) return true;
	return false;
}

// 초기입력정보 확인
//void Print()
//{
//	cout << endl;
//	for (int i = 0; i < MAX; i++) {
//		for (int j = 0; j < MAX; j++) {
//			cout << arr[i][j] << ' ';
//		}
//		cout << endl;
//	}
//	cout << endl;
//
//	for (int i = 0; i < 16; i++) {
//		cout << "fish[" << i << "]: " << fish[i].x << ' ' << fish[i].y << ' ' << fish[i].n << ' ' << fish[i].d << endl;
//	}
//}

void Copy_State(int A[][4], int B[][4], Fish C[], Fish D[])
{
	// 상어가 다음 턴 넘어갈때 현재 맵상태 저장하는 함수
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			A[i][j] = B[i][j];
		}
	}
	for (int i = 1; i <= 16; i++) C[i] = D[i];
}

void Make_State(int x, int y, int nx, int ny, int Fish_Num, bool T)
{
	if (T == true)
	{
		arr[nx][ny] = -1;
		arr[x][y] = 0;
		fish[Fish_Num].life = false;
	}
	else
	{
		arr[nx][ny] = Fish_Num;
		arr[x][y] = -1;
		fish[Fish_Num].life = true;
	}
}

void Swap_Fish(int Idx, int IIdx)
{
	Fish temp = fish[Idx];
	fish[Idx].x = fish[IIdx].x;
	fish[Idx].y = fish[IIdx].y;
	fish[IIdx].x = temp.x;
	fish[IIdx].y = temp.y;
}

void Move_Fish()
{
	// 모든 물고기 이동하기
	for (int i = 1; i <= 16; i++)
	{
		if (fish[i].life == false) continue;

		bool flag = false;
		int x = fish[i].x;
		int y = fish[i].y;
		int dir = fish[i].d;

		int nx = x + dx[dir];
		int ny = y + dy[dir];

		// 이동하려는 곳이 빈 칸인 경우
		if (Valid(nx, ny) && arr[nx][ny] == 0) {
			flag = true;
			fish[i].x = nx;
			fish[i].y = ny;
			arr[nx][ny] = i;
			arr[x][y] = 0;
		}
		// 이동하려는 곳에 물고기가 있는 경우
		else if (Valid(nx, ny) && arr[nx][ny] != -1) {
			flag = true;
			// 물고기 자리 바꾸기
			Swap_Fish(i, arr[nx][ny]);
			swap(arr[x][y], arr[nx][ny]);
		}

		// 해당 방향으로 이동을 못하는 경우
		if (flag == false)
		{
			int nDir = dir + 1;
			if (nDir == 9) nDir = 1;
			int nx = x + dx[nDir];
			int ny = y + dy[nDir];

			while (nDir != dir)
			{
				if (Valid(nx, ny))
				{
					if (arr[nx][ny] == 0)
					{
						fish[i].x = nx;
						fish[i].y = ny;
						arr[nx][ny] = i;
						arr[x][y] = 0;
						fish[i].d = nDir;
						break;
					}
					else if (arr[nx][ny] != -1)
					{
						Swap_Fish(i, arr[nx][ny]);
						swap(arr[x][y], arr[nx][ny]);
						fish[i].d = nDir;
						break;
					}
				}
				nDir++;
				if (nDir == 9) nDir = 1;
				nx = x + dx[nDir];
				ny = y + dy[nDir];
			}
		}
	}
}

// 상어가 물고기 먹는 로직
void DFS(int x, int y, int Dir, int Sum)
{
	Answer = Max(Answer, Sum);

	int C_MAP[4][4];
	Fish C_FISH[20];
	Copy_State(C_MAP, arr, C_FISH, fish);

	// 물고기 이동 함수
	Move_Fish();

	// 상어가 이동할 수 있는 모든 경우의 수 dfs탐색
	for (int i = 1; i <= 3; i++) {
		int nx = x + dx[Dir] * i;
		int ny = y + dy[Dir] * i;
		
		if (Valid(nx, ny)) {
			// 빈칸이면 pass
			if (arr[nx][ny] == 0) continue;

			int Fish_Num = arr[nx][ny];
			int nDir = fish[Fish_Num].d;

			// 상어가 물고기 잡아먹는 로직
			Make_State(x, y, nx, ny, Fish_Num, true);
			DFS(nx, ny, nDir, Sum + Fish_Num);
			Make_State(x, y, nx, ny, Fish_Num, false);
		}
		// 유효하지 않은 땅이면 탈출
		else break;
	}
	// 원래 상태로 되돌려 놓기
	Copy_State(arr, C_MAP, fish, C_FISH);
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	// 배열에 물고기 정보 초기화
	for (int i = 0; i < MAX; i++) {
		for (int j = 0; j < MAX; j++) {
			cin >> ai >> bi;
			arr[i][j] = ai;
			fish[ai] = { i,j,bi,true };
		}
	}

	//Print();
	
	// 상어 초기화
	int Fish_Num = arr[0][0];
	arr[0][0] = -1;
	fish[Fish_Num].life = false;
	int Dir = fish[Fish_Num].d;
	DFS(0, 0, Dir, Fish_Num);
	cout << Answer << endl;

	//// 모든 물고기 순서대로 이동하기
	//for (int i = 0; i < 16; i++)
	//{
	//	if (fish[i].life == true) 
	//	{
	//		int nx = fish[i].x + dx[fish[i].d];
	//		int ny = fish[i].y + dy[fish[i].d];
	//			
	//		// 이동할 수 있는 모든 방향 탐색
	//		for(int j=0; j<7; j++) {
	//			// 이동할 곳이 빈칸인 경우
	//			if (Valid(nx, ny) && arr[nx][ny] == 0) {
	//				arr[nx][ny] = fish[i].n;
	//				fish[i].x = nx;
	//				fish[i].y = ny;
	//				break;
	//			}
	//			// 이동할 곳에 물고기가 있는 경우
	//			else if (Valid(nx, ny) && arr[nx][ny] != 100) {
	//				pair<int, int> temp;
	//				int temp_num;

	//				temp_num = fish[i].n;
	//				temp = { nx, ny };
	//				fish[i].x = nx;
	//				fish[i].y = ny;


	//			}
	//		}
	//				
	//	}
	//}



	return 0;
}