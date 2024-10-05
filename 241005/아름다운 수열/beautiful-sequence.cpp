#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

int main() {
    int N;
    cin >> N;
    
    vector<int> A(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    int M;
    cin >> M;
    
    vector<int> B(M);
    for (int i = 0; i < M; ++i) {
        cin >> B[i];
    }
    
    // B를 정렬합니다.
    sort(B.begin(), B.end());

    vector<int> result; // 아름다운 수열의 시작 인덱스 저장
    int count = 0; // 아름다운 수열의 개수 카운트

    // A의 연속 부분 수열 탐색
    for (int i = 0; i <= N - M; ++i) {
        // A의 M 길이 부분 수열
        vector<int> subA(A.begin() + i, A.begin() + i + M);
        sort(subA.begin(), subA.end());

        // 두 수열 간의 차 계산
        int difference = subA[0] - B[0];
        bool isBeautiful = true;

        for (int j = 0; j < M; ++j) {
            if (subA[j] - B[j] != difference) {
                isBeautiful = false;
                break;
            }
        }

        if (isBeautiful) {
            result.push_back(i + 1); // 1-based index
            count++;
        }
    }

    // 결과 출력
    cout << count << endl;
    for (int idx : result) {
        cout << idx << endl;
    }

    return 0;
}