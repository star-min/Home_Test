//������ �Ǽ��� Ÿ��
//float - 4byte, double - 8byte, long double - 8byte
//�����ǹ����� Ÿ�� 
//(signed) char - 1byte, unsigned char - 2byte
#include <stdio.h>
int main(void){
	float pi = 3.1415;
	double area = 10*10*pi;
	char name = 'a';
	unsigned char irum = 'b'; 
	printf("\n�������� 10�� ���� �ѷ� ���̴� %.2f�Դϴ�.",10*2*pi);
	printf("\n�������� 10�� ���� ������ %.3f�Դϴ�.",area);
	printf("\n����� ������ %c��.", name);
	printf("\n����� �̸��� %c��.", irum);
	return 0;	
}
