#include <stdio.h>
int main(void){
	int num1 = 1234;
	double num2 = 3.14;
	int* pt_num1 = &num1; //�����Ϳ� ���Կ����� ���� �ּҸ� �־�� ��. 
	double* pt_num2 = &num2;	//&���� => �ּ� ������ 
	
	//1) pt_num1�� ���� ũ�⸦ ���
	printf("\n�������� ũ�� : %d",sizeof(pt_num1)); 
	//2) pt_num1�� ����Ű�� �ִ� �ּҸ� ���
	printf("\npt_num1�� ���� �ּ� : %#x", pt_num1);
	//3) pt_num2�� ����Ű�� �ִ� �ּҸ� ���
	printf("\npt_num2�� ���� �ּ� : %#x", pt_num2);
	//4) pt_num1�� ����Ű�� �ִ� �ּ��� ��ġ�� ����� ���� ���
	printf("\npt_num1�� �ּҰ� ����Ű�� �ִ� ������ : %d", *pt_num1);
	//5) pt_num2�� ����Ű�� �ִ� �ּ��� ��ġ�� ����� ���� ��� 
	printf("\npt_num2�� �ּҰ� ����Ű�� �ִ� ������ : %f", *pt_num2);
	return 0;
}
