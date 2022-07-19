#include	<stdio.h>
#include	<stdlib.h>
#include	<errno.h>
#include	<string.h>

/***our	old	friend	die	from	ex17.*/
void	die(const	char	*message)
{
	if(errno){
	
		perror(message);
		}else{
		printf("ERROR:	%s\n",message);
		}
		exit(1);


}

//a	typedef	creates	a	fake	type,in	this
//case	for	a	function	pointer

typedef	int	(*compare_cb)(int	a,	int	b);

/**
*A	classic	bubble	sort	function	that	uses	the
*compare_cb	to	do	the	sorting
*/
int	*bubble_sort(int	*numbers,int	count,compare_cb	cmp)
{
	int	temp=0;
	int	i=0;
	int	j=0;
	int	*target=malloc(count	*sizeof(int));





}
