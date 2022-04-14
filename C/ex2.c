//변수 : 기억장소의 이름 
//변수의 정수형 타입 : 
//unsigned short - 0~65535, signed short - -32,768 ~ 32,767 => 2byte
//unsigned int, signed int => 4byte
//unsigned long, signed long => 4byte
#include <stdio.h>
int main(void) {
	int num = 12345678907568915;	//overflow 발생 
	int age = 29;
	printf("변수 num의 저장된 데이터는 %d이며, 나이는 %d세 입니다.", num, age);
	return 0;	
}

