#include <stdio.h>
//����(�ּ�)�� ���� ����(call bt reference)
int local(int* num){
	*num+=10;
	return *num;
} 
int main(void){
	int var = 10;
	printf("\n���� var=%d", var);
	printf("\nlocal() �Լ� ȣ�� ���� var�� ����� : %d",local(&var));
	//int* num = &var;
	//�����͸� ����ϸ�, �迭�� ���� �⺻Ÿ��(primitive)�� �ƴ� ����Ÿ��(reference)��
	//Ȱ���� �� �־ �޸� Ȱ�뵵�� ��������. 
	int arr[2][3] = {{10,20,30},{40,50,60}};
	int *array1 = &arr;	//�ּ�(����)�� ���� ���� 
	printf(*array1); 
	return 0;
}
