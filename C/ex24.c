//1. 단수를 입력받아 구구단 중에서 해당 단의 결과를 출력하라
//입출력 예시)
// 단수 입력 : 3  <= 입력 예시
//	3*1=3	<= 출력 예시 
//	3*2=6
//	3*3=9
// ....
#include <stdio.h>
int main(void){
	int dan;
	printf("단 입력:");
	scanf("%d",&dan);
	int i;
	for(i=1;i<10;i++){
		printf("\n%d*%d=%d",dan,i,dan*i);
	}
	return 0;
} 
 


 
 
