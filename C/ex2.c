//���� : �������� �̸� 
//������ ������ Ÿ�� : 
//unsigned short - 0~65535, signed short - -32,768 ~ 32,767 => 2byte
//unsigned int, signed int => 4byte
//unsigned long, signed long => 4byte
#include <stdio.h>
int main(void) {
	int num = 12345678907568915;	//overflow �߻� 
	int age = 29;
	printf("���� num�� ����� �����ʹ� %d�̸�, ���̴� %d�� �Դϴ�.", num, age);
	return 0;	
}

