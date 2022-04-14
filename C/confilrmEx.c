#include <stdio.h>
int fac(int num){
	if(num == 1){
		return 1;
	}
	return num+fac(num-1);
}
int main(void){
	int num;
	printf("재귀를 통해 총 합을 구할 숫자 입력 : ");
	scanf("%d", &num);
	printf("결과 : %d", fac(num));
	return 0;
}
