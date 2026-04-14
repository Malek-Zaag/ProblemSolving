#include <stdio.h>
#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    int rev[n];
    for (int i = n - 1; i >= 0; i--)
    {
        rev[i] = arr[i];
        cout << rev[i] << " ";
    }
    return 0;
}