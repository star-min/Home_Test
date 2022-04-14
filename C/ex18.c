#include <stdio.h>
//2차원 배열 : 타입  배열명[행의수][열의수] = {{열값1,열값2,..},{열값1,열값2,..}}; 
//5명의 번호, 국어, 영어, 수학을 배열변수로 입력받아
//개인 총점, 개인 평균, 개인 학점, 개인 석차를 계산하고,
//모든 사람의 점수와 총점, 평균, 학점, 석차를 출력하고,
//과목별 총점, 과목별 평균, 과목별 최대값, 과목별 최소값을 출력
int main(void){
	int jum[5][4] = {{1,90,80,70},{2,100,90,80},{3,80,75,80},{4,90,100,100},{5,75,100,85}};
	int tot[5] = {0,0,0,0,0};	//개인 총점 
	float avg[5] = {0.0f,0.0f,0.0f,0.0f,0.0f};	//개인 평균 
	char hak[5] = {'A','A','A','A','A'};	//개인 학점
	int rank[5] = {1,1,1,1,1};	//개인 석차 
	int hap[3] = {0,0,0};	//과목별 총점 
	float py[3] = {0.0f,0.0f,0.0f}; //과목별 평균 
	int max[3] = {0,0,0};	//과목별 최대값 
	int min[3] = {100,100,100};	//과목별 최소값
	int i,j;
	for(i=0;i<5;i++){
		for(j=1;j<4;j++){
			tot[i]+=jum[i][j];	//개인 총점 
			hap[j-1]+=hap[j-1]+jum[i][j];	//과목별 총점 
		}
		avg[i] = (float) tot[i] / 3;	//개인 평균 
		if(avg[i]>=90){	 hak[i] = 'A'; } else if(avg[i]>=80){ hak[i] = 'B';	}
		else if(avg[i]>=70){ hak[i] = 'C'; } else if(avg[i]>=60){ hak[i] = 'D';	}
		else { hak[i] = 'F'; }		//개인 학점
	}
	for(i=0;i<5;i++){	//개인 석차 
		for(j=0;j<5;j++){ if(tot[i]<tot[j]){	rank[i]+=1;	}	}
	}
	for(j=0;j<3;j++){	py[j] = (float) hap[j] / 5; } //과목별 평균 
	for(i=0;i<3;i++){
		for(j=0;j<5;j++){
			if(max[i] < jum[j][i+1]) {	 max[i] = jum[j][i+1];	}//과목별 최대값
			if(min[i] > jum[j][i+1]) {	min[i] = jum[j][i+1];	}//과목별 최소값
		}
	}
	printf("번호\t\t국어\t영어\t수학\t총점\t평균\t학점\t석차\n");
	for(i=0;i<5;i++){
		printf("%d\t\t%d\t%d\t%d\t%d\t%.2f\t%c\t%d\n", jum[i][0], 
		jum[i][1],jum[i][2],jum[i][3],tot[i],avg[i],hak[i],rank[i]);
	}
	printf("과목별총점\t%d\t%d\t%d\n",tot[0],tot[1],tot[2]);
	printf("과목별평균\t%.2f\t%.2f\t%.2f\n",avg[0],avg[1],avg[2]);
	printf("과목별 최대값\t%d\t%d\t%d\n",max[0],max[1],max[2]);
	printf("과목별 최소값\t%d\t%d\t%d\n",min[0],min[1],min[2]);
	return 0;
}

