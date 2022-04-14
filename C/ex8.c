//비교 연산자 : 변수에 담긴 내용과 특정  값과 비교하는 연산자로 결과로 논리값이 출력됨
#include <stdio.h>

int main(void){
	int num1 = 10;
	int num2 = 20;
	char data1 = 'a';	//문자 
	char data2[4] = "kim";  //문자열 
	//글자수보다 하나 더 크게 = 글자수+1 만큼 배열로 설정해야함 
	
	printf(num1 > num2);
	printf(num1 >= num2); 
	printf(num1 < num2);
	printf(num1 <= num2);
	printf(num1 == num2);
	printf(num1 != num2);
	return 0;
} 
