#include <stdio.h>
int rAdd(int n){ //�Լ� - �����ƾ 
	if(n == 1) {
		return 1;
	}
	return n+rAdd(n-1);
}
int main(void){
	int data;
	printf("����� ���ڸ� �Է� : ");
	scanf("%d", &data); 
	printf("��� : %d", rAdd(data));
	return 0;
} 
