//1. �ܼ��� �Է¹޾� ������ �߿��� �ش� ���� ����� ����϶�
//����� ����)
// �ܼ� �Է� : 3  <= �Է� ����
//	3*1=3	<= ��� ���� 
//	3*2=6
//	3*3=9
// ....
#include <stdio.h>
int main(void){
	int dan;
	printf("�� �Է�:");
	scanf("%d",&dan);
	int i=1;
	while(i<10){
		printf("\n%d*%d=%d",dan,i,dan*i);
		i++;
	}
	return 0;
} 