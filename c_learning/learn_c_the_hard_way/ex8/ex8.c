#   include<stdio.h>

int main(int    argc,char   *argv[])
{
    int areas[]={0,10,20,30,40,50};
    char name[]="zed";
    char full_name[]={'Z','e','d',' ','A','.',' ','S','h','A','w'};
    
    printf("The size of an int %ld\n",sizeof(int));
    printf("The size of areas (int[]) %ld\n",sizeof(areas));
    printf("The number of ints in areas :%ld\n",sizeof(areas)/sizeof(int));
    printf("The first area is %d and the second is %d\n",areas[0],areas[1]);
    printf("The size of a char is %ld\n",sizeof(char));
    printf("The size of name (char[]) :%ld\n",sizeof(char));
    printf("The number of char : %ld\n",sizeof(name)/sizeof(char));
    printf("The size of fullname (char[]) : %ld\n",sizeof(full_name));
    printf("The size of chars : %ld\n", sizeof(char));
    printf("name = \"%s\" and full_name = \"%s\"\n",name,full_name);
    return 0;
    
}
