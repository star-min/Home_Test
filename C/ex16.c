#include <stdio.h>
//�Լ��� : sum
//�Լ� ó������ : 1���� Ű����� �Է��� ���ڸ�ŭ ���Ͽ� ��ȯ�ϴ� ���α׷��� �ۼ�
int sum(int n){	//�Լ��� ����� ���� 
	int i, res = 0; 	//1~n������ �հ踦 ����Ͽ� ��ȯ
	for(i=1;i<=n;i++){		res+=i; 	}
	return res;
}
//��� ȣ�� �Լ�(recursive call function) : �ڱ� �ڽ��� �ݺ� ȣ��
int rSum(int n){
	if(n==1){		return 1;	}
	return n+rSum(n-1);
} 
//����, 20������ �հ踦 ���ÿ� �ڱ��ڽ��� ���ȣ���Ͽ� 20+19+18+17+16+15,....���·� 
//�ݺ� �����ϰԵ� 
int main(void){
	int data; 
	printf("���� �Է� : ");
	scanf("%d",&data);
	printf("1���� %d�� �հ� : %d", data, sum(data));	//�Լ� ȣ�� 
	return 0;
}
