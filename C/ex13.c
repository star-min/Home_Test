//for�� - for(�ʱⰪ;���ǽ�;������) { ���๮��; }
#include <stdio.h>
int main(void){
	//1~100������ Ȧ���� �հ� ����Ͽ� ����ϴ� �ݺ��� ���೻���� �ۼ� 
	//for, continueȰ�� 
	int tot = 0, i;
	for(i=0;i<100;i++){
		if(i % 2 == 0){
			continue;
		}
		tot+=i;
	} 
	printf("\n1~100 �հ� : %d\n", tot);
	//������ ��� - ���� for�� 
	//2*1=2		3*1=3....... 
	//2*2=4		.......
	//......
	printf("*********************************\n");
	printf("\t\t������ \n");
	printf("*********************************\n");
	int a,b;
	for(a=1;a<10;a++){
		for(b=2;b<10;b++){
			printf("%d*%d=%d\t",b,a,a*b);	
		}
		printf("\n");
	}
	return 0;
} 
