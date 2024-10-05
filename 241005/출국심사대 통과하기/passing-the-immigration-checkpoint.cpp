#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    int time = 0;
    cin >> N;
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>> > q;
    for (int i=0; i<N; ++i){
        int arrivedTime, spendingTime;
        cin >> arrivedTime >> spendingTime;
        q.push({arrivedTime,spendingTime});
    }
    while(!q.empty()){
        auto customer = q.top();
        q.pop();
        if (customer.first > time){
            time = customer.first;
        }
        time += customer.second;
    }
    cout << time;
    return 0;
}