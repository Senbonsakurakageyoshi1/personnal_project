#include<stdio.h>//input output library
#include<assert.h>// call abort if the assert condition is false and exit the current program
#include<stdlib.h>
#include<string.h>

struct	Person{ // define the structure Person
	char	*name;
	int	age;
	int height;
	int	weight;
	

};



struct	Person	*Person_create(char	*name,int	age,int	height,int	weight) // construction method of person
{
	struct	Person	*who=malloc(sizeof(struct	Person));// allocate a memory of size of the Person structure and create a 
	//wich point to a the allocated memory
	assert(who	!=	NULL); // verify it's a correct pointer
	who->name	=	strdup(name);//modify the name strut's variable
	who->age	=	age;// modify the age struct's variable
	who->height	=	height;// modify the height struct's variable
	who->weight	=	weight;// modify the weight struct's variable
	
	return	who;// return the pointer to the allocated memory for the Person structure
	
}


void	Person_destroy(struct	Person	*who)// function of destruction of person which take's the Person structure 
{
	assert	(who	!=	NULL);//verify it's a good pointer
	free	(who	->	name);// erase the name
	free(who);// erase all the person
	
	}
	
void	Person_print(struct	Person	*who)// function for printing person wich take's the struct person in parameter
{
	printf("Name:	%s\n",who->name);
	printf("\tAge:%d\n",who->age);
	printf("\tHeight:%d\n",who->height);
}

int	main(int	argc,char	*argv[])
{
		//make	two	people	structures
		
		struct	Person	*joe=	Person_create("joe	Alex",32,64,140);//create the person joe
		struct	Person	*franck	=	Person_create("Frank	Blank",20,72,180);//create the person franck
		
		//print	the	out	and	where	they	are	in	memory
		
		printf("joe	is	at	memory	location	%p:\n",joe);
		Person_print(joe);
		
		printf("Frank is at memory	location	%p:\n",franck);
		Person_print(franck);
		
		//make every one 20 years and print	them	again
		printf("here is the initial value of the age of joe and franck\t : %d  and  %d",joe->age,franck->age);
		joe->age	+=20;
		joe->height	-=2;
		joe->weight	+=40;
		Person_print(joe);
		
		franck->age	+=20;
		franck->weight	+=20;
		Person_print(franck);
		
		//destroy	them	so	we	clean	up
		
		Person_destroy(joe);
		Person_destroy(franck);
		return	0;
}


