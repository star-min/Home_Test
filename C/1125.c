#include <stdio.h>
int main()
{
	int i;
	int j = 0;
	for(i=1;i<=10;i++){
		if(i%2==1){
			j+=i;
		}else{
			j-=i;
		}
	}
	printf("%d",j);
	return 0;
}
