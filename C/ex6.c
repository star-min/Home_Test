#include <stdio.h>
//연산자 : 산술, 대입, 증감, 비교, 논리, 비트, 기타 
int main(void){
	int num1 = 10;
	int num2 = 5;
	int num3 = 20;
	int num4 = 30;
	printf("\nnum1+num2=%d", num1+num2);
	printf("\nnum1-num2=%d", num1-num2);
	printf("\nnum1*num2=%d", num1*num2);
	printf("\nnum1/num2=%d", num1/num2);
	printf("\nnum1 나눈나머지 num2=%d", num1%num2);
	num3+=5;	//num3=num3+5;
	printf("\nnum3+=5 의 결과 : %d", num3);
	num4-=5;	//num4=num4-5
	printf("\nnum4-=5 의 결과 : %d", num4);
	num3*=3;	//num3=num3*3;
	printf("\nnum3*=3 의 결과 : %d", num3);
	num4/=3;	//num4=num4/3;
	printf("\nnum4/=3 의 결과 : %d", num4);
	num3%=5;	//num3=num3%5;
	printf("\nnum3%%=5 의 결과 : %d", num3);
}
