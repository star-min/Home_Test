#include <stdio.h>
//������ : ���, ����, ����, ��, ��, ��Ʈ, ��Ÿ 
int main(void){
	int num1 = 10;
	int num2 = 5;
	int num3 = 20;
	int num4 = 30;
	printf("\nnum1+num2=%d", num1+num2);
	printf("\nnum1-num2=%d", num1-num2);
	printf("\nnum1*num2=%d", num1*num2);
	printf("\nnum1/num2=%d", num1/num2);
	printf("\nnum1 ���������� num2=%d", num1%num2);
	num3+=5;	//num3=num3+5;
	printf("\nnum3+=5 �� ��� : %d", num3);
	num4-=5;	//num4=num4-5
	printf("\nnum4-=5 �� ��� : %d", num4);
	num3*=3;	//num3=num3*3;
	printf("\nnum3*=3 �� ��� : %d", num3);
	num4/=3;	//num4=num4/3;
	printf("\nnum4/=3 �� ��� : %d", num4);
	num3%=5;	//num3=num3%5;
	printf("\nnum3%%=5 �� ��� : %d", num3);
}
