//표준 입력 : scanf("입력인자", &저장변수명); 
#include <stdio.h>
//#define MAX 10; - 매크로 상수 : 다른 함수에서도 활용이 가능함 
int main(void){
	//const MAX = 10; - 심볼릭 상수 : 현재 함수에서만 활용이 가능함 
	int num1, num2;
	printf("숫자1 입력 : ");
	scanf("%d", &num1); 
	printf("숫자2 입력 : ");
	scanf("%d", &num2);
	printf("숫자1 + 숫자2 = %d",num1+num2);
	int num3, num4;
	printf("두 개의 정수를 입력 : ");
	scanf("%d, %d", &num3, &num4);
	printf("\n8진수로 변환: %o, %o", num3, num4);
	printf("\n16진수로 변환: %x, %x", num3, num4); 
	return 0;
	//입출력 인자 문자(입출력 변환 문자)
	//%d : 10진수 정수, %o : 8진수 정수, %x:16진수 정수,  %c : 문자, %s : 문자열
	//%f : 실수로 출력
	//2*10의 6승 -> 지수형식
	//%e -> 2e+10, %E -> 2E+10
	//%ld : long 타입의 정수, %lo : long 타입의 8진수
	//%lx : long 타입의 16진수, %u : 부호없이 10진수로 출력 
} 
