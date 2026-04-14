#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;

void update(int *a, int *b)
{
    int temp = *a;
    int temp2 = *b;
    *a = *a + *b;
    *b = std::abs(temp2 - temp);
}

int main()
{
    int a, b;
    int *pa = &a, *pb = &b;

    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}