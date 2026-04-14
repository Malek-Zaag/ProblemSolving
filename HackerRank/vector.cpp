#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

// int main()
// {
//     int n, q;
//     cin >> n >> q;
//     vector<vector<int>> mat;
//     for (int j = 0; j < n; j++)
//     {
//         int l;
//         cin >> l;
//         vector<int> v(l);
//         for (int i = 0; i < l; i++)
//         {
//             cin >> v[i];
//         }
//         mat[j] = v;
//     }
//     for (int i = 0; i < q; i++)
//     {
//         int x, y;
//         cin >> x >> y;
//         cout << mat[x][y];
//         cout << endl;
//     }
//     return 0;
// }
int main()
{
    int n, q;
    cin >> n >> q;
    vector<vector<int>> mat(n);
    for (int row = 0; row < n; row++)
    {
        int l;
        cin >> l;
        mat[row].resize(l);
        for (int j = 0; j < l; j++)
        {
            cin >> mat[row][j];
        }
    }

    for (int i = 0; i < q; i++)
    {
        int x, y;
        cin >> x >> y;
        cout << mat[x][y] << endl;
    }

    return 0;
}