#include<bits/stdc++.h>
#include<ext/pb_ds/assoc_container.hpp>
#include<ext/pb_ds/tree_policy.hpp>
#include<algorithm>
#include<unordered_map>
#include<vector>
#include<unordered_set>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include<map>
#include<chrono>

using namespace std;
using namespace __gnu_pbds;
using namespace chrono;
#define fastio() ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
#define nline "\n"
#define ll long long
/*---------------------------------------------------------------------------------------------------------------------------*/
ll gcd(ll a, ll b) {
    if (b > a) { return gcd(b, a); }
    if (b == 0) { return a; }
    return gcd(b, a % b);
}

vector<int> sieve(int n) {
    int *arr = new int[n + 1]();
    vector<int> vect;
    for (int i = 2; i <= n; i++)
        if (arr[i] == 0) {
            vect.push_back(i);
            for (int j = 2 * i; j <= n; j += i)arr[j] = 1;
        }
    return vect;
}

vector<vector<int>> readMatrix(int n, int m) {
    vector<vector<int>> v;
    for (int i = 0; i < n; i++) {
        vector<int> y;
        for (int j = 0; j < m; j++) {
            int x;
            cin >> x;
            y.push_back(x);
        }
        v.push_back(y);
    }
    return v;
}

/*--------------------------------------------------------------------------------------------------------------------------*/
void solve() {
    
    return;

}

int main() {
    fastio();
    auto start1 = high_resolution_clock::now();
    solve();
    auto stop1 = high_resolution_clock::now();
    return 0;
}//
// Created by Malek on 02/08/2022.
//
