#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int sum(int a, int b) {
	return a+b;
}

void print(int a, int b){
	if(b){
		printf("계산결과:%d",a);
	}
}

int main(){
	int result=sum(105,250);
	print(result,"b");
	return 0;
}
