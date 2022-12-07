#include
int main()
{
	int i;
	int j = 0;
	for(i=1;i<=5;i++){
		if(i%2==1){
			j+=i;
		}else{
			j-=i;
		}
	}
	printf("%d",j);
	return 0;
}
