#include <stdio.h>
//scope : ������ ������ ��ȿ���� 
void local(void);	//�ڹٿ����� �������̽� 
int main(void){
	int i = 5;
	int var = 10; 
	
	printf("main()�Լ� ���� �������� var�� ���� %d\n", var);
	if(i<10){
		local();
		int var = 30;
		printf("if�� ���� �������� var�� ���� %d\n", var);
	}
	return 0;
}
void local(void){	//�ڹٿ����� Ŭ���� 
	int var = 20;
	printf("local()�Լ� ���� �������� var�� ���� %d\n", var);
}
