//비트연산자 : 2진수 연산, &, |, ^, ~, <<, >>
#include <stdio.h>
int main(void){	//	16	8	4	2	1
	int a = 10;	//	0	1	0	1	0
	int b = 20;	//	1	0	1	0	0
	int c = a & b;//0	0	0	0	0
	int d = a | b;//1	1	1	1	0
	int e = a ^ b;//1	1	1	1	0
	int f = ~a;	//	1	0	1	0	1
	int g = b >> 2;//1	0	1	0	0 -> 20
				//	0	1	0	1	0 -> 10	
				//	0	0	1	0	1 -> 5
	int h = b << 2;//1	0	1	0	0 -> 20
				//1	0	1	0	0	0 -> 40
			//1	0	1	0	0	0	0 -> 80
	printf("\na & b = %d", c);
	printf("\na | b = %d", d);
	printf("\na ^ b = %d", e);
	printf("\n~a = %d", f);
	printf("\nb >> 2 = %d", g);
	printf("\nb << 2 = %d", h);
	
	int i = (a > b) ? a : b;
	int j=30, k=40;	//쉼표 연산자 
	printf("\na와 b중에서 더 큰값은 : %d", i);
	printf("\na의 크기 : %d", sizeof a); 
	return 0;
} 
