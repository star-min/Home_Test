#include <stdio.h>
int rAdd(int n){ //함수 - 서브루틴 
	if(n == 1) {
		return 1;
	}
	return n+rAdd(n-1);
}
int main(void){
	int data;
	printf("계산할 숫자를 입력 : ");
	scanf("%d", &data); 
	printf("결과 : %d", rAdd(data));
	return 0;
} 
