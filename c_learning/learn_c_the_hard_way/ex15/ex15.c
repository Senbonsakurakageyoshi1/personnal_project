#include	<stdio.h>

int	main(int	argc,char	*argv[])
{
	//create	two	array	we	care	about
	int	ages[]	=	{23,43,12,89,2};
	char	*name[]	=	{"Alan","Franck","Mary","John","Lisa"};
	
	//safely	get	the	size	of	ages
	int	count	=	sizeof(ages)/sizeof(int);
	int	i=0;
	//first	way	using	indexing
	printf("voici	count et size of int	======>%d  %d\n",sizeof(int),count);
	for(i=0;i<count;i++){
		printf("%s	has	%d	years	alive.\n",name[i],ages[i]);
		}
		
	printf("___\n");
	
	//setup	the	pointers	to	the	start	of	the	arrays
	
	int	*cur_age=ages;
	char	**cur_name=name;
	
	//second	way	using	pointers
	
	for(i=0;i<count;i++){
	
	printf("Here is cur_name : %d\n",**cur_name);
	printf("%s	is	%d	years	old.\n",*(cur_name+i),*(cur_age+i));
	}
	
	
	printf("----\n");
	
	//third way,pointers	are	just	arrays
	
	for(i=0;i<count;i++){
		printf("%s	is	%d	years	old	again.\n",cur_name[i],cur_age[i]);
		}
		
	printf("----\n");
	
	//fourth	way	with	pointers	in	a	stupid	complex	way
	
	for(cur_name=name,cur_age=ages;(cur_age-ages)<count;cur_name++,cur_age++)
	{
		printf("%s	lived	%d	years	so	far.\n",*cur_name,*cur_age);
		
		}
		
		return 0;
		
		

			
	
}
