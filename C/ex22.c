#include <stdio.h>
int local(int num){
	num+=10;
	return num;
}
int main(void){
	int var = 10;
	printf("\n���� var�� �ʱⰪ : %d", var);
	printf("\nlocal() �Լ� ȣ�� ���� ���� var�� ���� %d ��\n", local(var));
	//local(��) ���·� ȣ���Ͽ� local�Լ��� ���� �����Ͽ� ������ �� �ٽ� ���� ����
	//�ް� �� => ���� ���� ����(Call by value) 
	return 0; 
}
