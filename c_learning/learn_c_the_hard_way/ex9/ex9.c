#include	<stdio.h>

int	main(int	argc,char	*argv[])
{
	int	numbers[4]={0};
	char	name[5]={'a'};
	
	printf("numbers:%d,%d,%d,%d",numbers[0],numbers[1],numbers[2],numbers[3]);
	printf("\neach letters	:%c,%c,%c,%c",name[0],name[1],name[2],name[3]);
	printf("\nname:%s",name);
	
	
	
	numbers[0]=1;
	numbers[1]=2;
	numbers[2]=3;
	numbers[3]=4;
	
	name[0]='N';
	name[1]='A';
	name[2]='G';
	name[3]='A';
	name[4]='\0';
	printf("\nnumbers:%d,%d,%d,%d,%d",numbers[0],numbers[1],numbers[2],numbers[3]);
	printf("\neach letters	:%c,%c,%c,%c",name[0],name[1],name[2],name[3]);
	printf("\nname:%s",name);
	printf("\nnumbers:%d",numbers);
	
	char	*another	=	"NAGA";
	printf("\nanother :%s",another);
	printf("\nanother	each:%c,%c,%c,%c",another[0],another[1],another[2],another[3]);
	return	0;
}
