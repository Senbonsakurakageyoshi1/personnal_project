#include <studio.h>


har x =1;
int i;

void foo(char y )
{

    char a  =2;
    static char v = 5;
    v=a+y;

}


void main(void)
{

    char j  =5;
    i=i+x;
    printf("%d",i);

    foo(i);
}

