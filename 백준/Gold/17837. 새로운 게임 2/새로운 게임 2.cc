#include <iostream>
#include <vector>

#define MAX 12
#define endl "\n"

using namespace std;

// 말 객체 선언
struct horse {
	int r;
	int c;
	int d;
};

// 말 위치 보드판, 말 정보 구조체 벡터, 보드판 선언
vector<int> horse_arr[MAX][MAX];
horse horse_home[10];
int arr[MAX][MAX];

int dx[5] = { 0, 0, 0, -1, 1 }; // 우좌상하
int dy[5] = { 0, 1, -1, 0, 0 };

int n, k;
bool Flag = false;

void Print()
{
	cout << "보드판 입력정보를 확인합니다\n";
	// 보드판 입력정보 확인하기
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cout << arr[i][j] << ' ';
		}
		cout << '\n';
	}
	cout << endl;
	// 보드판에 존재하는 말 갯수 확인하기
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cout << horse_arr[i][j].size() << ' ';
		}
		cout << '\n';
	}
}

// 맵의 범위 체크해주기
bool Valid(int x, int y)
{
	if (x >= 0 && y >= 0 && x < n && y < n) return true;
	return false;
}

int FindPosition(int x, int y, int idx)
{
	for (int i = 0; i < horse_arr[x][y].size(); i++) {
		if (horse_arr[x][y][i] == idx) return i;
	}
}

int Find_Delete_Num(int x, int y, int horse_num)
{
	int Cnt = 0;
	for (int i = horse_arr[x][y].size() - 1; i >= 0; i--) {
		if (horse_arr[x][y][i] == horse_num) break;
		Cnt++;
	}
	return Cnt + 1;
}

int ReversDir(int num)
{	
	int dir = horse_home[num].d;
	if (dir == 1) return 2;
	else if (dir == 2) return 1;
	else if (dir == 3) return 4;
	else if (dir == 4) return 3;

}

void MoveHorse(int r, int c, int nr, int nc, int Idx, int Pos, int Ms)
{
	// 이동하려는 땅이 흰색인경우
	if (Ms == 0)
	{
		// 움직이려는 말위에 쌓여있는 말이랑 같이 이동하기
		for (int i = Pos; i < horse_arr[r][c].size(); i++) {
			horse_arr[nr][nc].push_back(horse_arr[r][c][i]);
			horse_home[horse_arr[r][c][i]].r = nr;
			horse_home[horse_arr[r][c][i]].c = nc;
		}
		// 말 이동후 원래 있던 위치에 있는 말 삭제하기
		int Delete_Num = Find_Delete_Num(r, c, Idx);
		for (int i = 0; i < Delete_Num; i++) horse_arr[r][c].pop_back();
	}
	// 이동하려는 땅이 빨간색인 경우
	else if (Ms == 1)
	{
		// 이동하려는 말부터 이동할 곳에 반대로 쌓기
		for (int i = horse_arr[r][c].size() - 1; i >= Pos; i--)
		{
			horse_arr[nr][nc].push_back(horse_arr[r][c][i]);
			horse_home[horse_arr[r][c][i]].r = nr;
			horse_home[horse_arr[r][c][i]].c = nc;
		}
		// 말 이동후 원래 있던 위치에 있는 말 삭제하기
		int Delete_Num = Find_Delete_Num(r, c, Idx);
		for (int i = 0; i < Delete_Num; i++) horse_arr[r][c].pop_back();
	}
	// 이동하려는 땅이 파란색 혹은 장외인 경우
	else if (Ms == 2)
	{
		int Dir = ReversDir(Idx);
		horse_home[Idx].d = Dir;

		int nnr = r + dx[Dir];
		int nnc = c + dy[Dir];

		if (Valid(nnr, nnc)) {
			if (arr[nnr][nnc] != 2) {
				MoveHorse(r, c, nnr, nnc, Idx, Pos, arr[nnr][nnc]);
			}
		}
	}
}

bool Check_State()
{
	for (int i = 0; i < k; i++)
	{
		int x = horse_home[i].r;
		int y = horse_home[i].c;
		if (horse_arr[x][y].size() >= 4) return true;
	}
	return false;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> k;

	// 보드판 입력받기
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> arr[i][j];
		}
	}

	// 말 정보 입력받기
	// vector의 push_back을 사용하기 때문에 디폴트값은 0으로 설정
	for (int i = 0; i < k; i++) {
		horse h;
		cin >> h.r >> h.c >> h.d;
		h.r--; h.c--; // 배열 시작값이 0이므로 행열값을 -1씩 해줘야한다.
		horse_arr[h.r][h.c].push_back(i);
		horse_home[i] = { h };
	}

	//Print();

	int turnCnt = 0;
	// 새로운게임 시뮬레이션
	while (true)
	{
		if (turnCnt > 1000) break;

		// 격자위에 있는 말 번호 순서대로 이동하기
		for (int i = 0; i < k; i++) {
			// 말의 현재 위치 정보
			int r = horse_home[i].r;
			int c = horse_home[i].c;
			int d = horse_home[i].d;
			
			// 말이 이동할 좌표 위치
			int nr = r + dx[d];
			int nc = c + dy[d];

			// 말의 번호
			int Idx = i;

			// 말이 보드판에서 몇 번째에 쌓여있는지 찾아서 반환
			int Pos = FindPosition(r, c, i);

			// 보드판 장외가 아니면
			if (nr >=0 && nc>=0 && nr < n && nc < n) MoveHorse(r, c, nr, nc, Idx, Pos, arr[nr][nc]);
			else MoveHorse(r, c, nr, nc, Idx, Pos, 2);

			// 말이 4개 이상 쌓였으면 종료하기
			if (Check_State() == true)
			{
				Flag = true;
				break;
			}
		}
		if (Flag == true) break;
		turnCnt++;
	}

	if (Flag == true) cout << turnCnt + 1 << endl;
	else cout << -1 << endl;

	return 0;
}