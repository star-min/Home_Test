//for문 - for(초기값;조건식;증감식) { 실행문장; }
#include <stdio.h>
int main(void){
	//1~100까지의 홀수의 합계 계산하여 출력하는 반복문 실행내용을 작성 
	//for, continue활용 
	int tot = 0, i;
	for(i=0;i<100;i++){
		if(i % 2 == 0){
			continue;
		}
		tot+=i;
	} 
	printf("\n1~100 합계 : %d\n", tot);
	//구구단 출력 - 이중 for문 
	//2*1=2		3*1=3....... 
	//2*2=4		.......
	//......
	printf("*********************************\n");
	printf("\t\t구구단 \n");
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
