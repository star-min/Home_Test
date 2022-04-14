//반복문 : 같은 구문을 여러 번 실행해야하는 경우 활용하는 문장 - while/do~while/for
//무한루프 : 항상 조건이 만족하여 무한정 계속 실행을 반복하는 구조 
#include <stdio.h>
int main(void){
	int i = 0;
	while(i<10){
		printf("\ni=%d", i);
		i++; 
	}
	printf("\n최종 i는 %d", i);
	return 0;
	
	int j = 0;
	printf("\n");
	//무조건 한 번은 실행을 할 수 있도록 하는 구조 - do~while 
	do {
		j++;
		printf("\nj=%d", j);
	} while(j>10);
	printf("\n최종j=%d", j);
}
 
