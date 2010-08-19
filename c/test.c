#include <stdio.h>

int add(int x, int y)
{
    int z;
    z = x + y;
    return z;
}

int main(void)
{
    int a, b, c;

    a = 3;
    b = 4;
    c = add(a, b);
    printf("a + b =%d\n", c);

    return 0;
}
