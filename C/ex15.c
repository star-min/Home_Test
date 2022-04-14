#include <stdio.h>
//scope : 변수가 가지는 유효범위 
void local(void);	//자바에서는 인터페이스 
int main(void){
	int i = 5;
	int var = 10; 
	
	printf("main()함수 내의 지역변수 var의 값은 %d\n", var);
	if(i<10){
		local();
		int var = 30;
		printf("if문 내의 지역변수 var의 값은 %d\n", var);
	}
	return 0;
}
void local(void){	//자바에서는 클래스 
	int var = 20;
	printf("local()함수 내의 지역변수 var의 값은 %d\n", var);
}
