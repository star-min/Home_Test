//�Լ� : �ʿ��� ����� ��� ���Ͽ� ������ ���� �Ź� ���� ������ ó���ؾ� �� ���
//Ư���̸����� ������ �� �ʿ��� �� ���� ȣ���Ͽ� ����ϴ� ����
#include <stdio.h>		//����ó���� 
//�Լ�����
//��ȯŸ��  �Լ���(Ÿ�� �Ű�����1, Ÿ�� �Ű�����2,... Ÿ��  �Ű�����n)  { ���๮; } 
int bigNum(int num1, int num2){
	if(num1 > num2) {
		return num1;
	} else {
		return num2;
	}
}
int main(void){
	int res;
	int a=100, b=200, c=150, d=250;
	res = bigNum(a, b);		//ȣ�� 
	printf("ū �� : %d", res);
	return 0;
}
