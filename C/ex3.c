//변수의 실수형 타입
//float - 4byte, double - 8byte, long double - 8byte
//변수의문자형 타입 
//(signed) char - 1byte, unsigned char - 2byte
#include <stdio.h>
int main(void){
	float pi = 3.1415;
	double area = 10*10*pi;
	char name = 'a';
	unsigned char irum = 'b'; 
	printf("\n반지름이 10인 원의 둘레 길이는 %.2f입니다.",10*2*pi);
	printf("\n반지름이 10인 원의 면적은 %.3f입니다.",area);
	printf("\n당신의 네임은 %c임.", name);
	printf("\n당신의 이름은 %c임.", irum);
	return 0;	
}
