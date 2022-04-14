//함수 : 필요한 결과를 얻기 위하여 복잡한 식을 매번 같은 내용을 처리해야 할 경우
//특정이름으로 정의한 후 필요할 때 마다 호출하여 사용하는 형태
#include <stdio.h>		//선행처리기 
//함수문법
//반환타입  함수명(타입 매개변수1, 타입 매개변수2,... 타입  매개변수n)  { 실행문; } 
int bigNum(int num1, int num2){
	if(num1 > num2) {
		return num1;
	} else {
		return num2;
	}
}
int main(void){
	int res;
	int a=100, b=200, c=150, d=250;
	res = bigNum(a, b);		//호출 
	printf("큰 값 : %d", res);
	return 0;
}
