#include <stdio.h>
int fac(int num){
	if(num == 1){
		return 1;
	}
	return num+fac(num-1);
}
int main(void){
	int num;
	printf("��͸� ���� �� ���� ���� ���� �Է� : ");
	scanf("%d", &num);
	printf("��� : %d", fac(num));
	return 0;
}
