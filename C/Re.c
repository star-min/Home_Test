#include <stdio.h>

int factorial(int n){
	if (n==1){
		return 1;	
	}
	return n*factorial(n-1);
}
int main(){
	int num, sum;
	scanf("%d",&num);
	sum=factorial(num);
	printf("%d\n",sum);
	return 0;
}
