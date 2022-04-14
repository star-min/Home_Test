//논리 연산자 : &&, ||, !
#include <stdio.h>
int main(void){
	int a = 10;
	int b = 20;
	int c = 30;
	printf("\n");
	printf(a<b && b<c);	//true
	printf("\n");
	printf(a>b && b<c);	//false
	printf("\n");
	printf(a<b && b>c);	//false
	printf("\n");
	printf(a>b && b>c);	//false
	printf("\n");
	printf(a<b || b<c);	//true
	printf("\n");
	printf(a>b || b<c);	//true
	printf("\n");
	printf(a<b || b>c);	//true
	printf("\n");
	printf(a>b || b>c);	//false
	printf("\n");
	printf(!(a>b));		//true
	printf("\n");
	printf(!(a<b));		//false
	printf("\n");
	return 0;
} 
