//4. 5명의 전산, OA, PG의 점수와 번호를 배열로 입력받아 해당 학생들의 
//개인총점, 개인 평균, 학점, 석차를 계산하여 출력하는 프로그램을 작성 하라
//단, 석차는 개인 총점이 가장 큰 사람이 석차가 1등이며, 학점은 90점이상(A), 
//80~89점(B), 70~79점(C), 60~69점(D) 나머지는 F로 한다.
//개인 총점 = 전산(EDPS)점수+OA점수+PG점수
//개인 평균 = 개인 총점 / 과목수
#include <stdio.h>
int main(void){
	int i, j;
	int num[5]={1,2,3,4,5};
	int edps[5]={100,90,95,85,90};
	int oa[5]={95,85,80,90,100};
	int pg[5]={90,85,100,90,85};
	int tot[5] = {0,0,0,0,0};
	double avg[5] = {0.0,0.0,0.0,0.0,0.0};
	char hak[5] = {'A','A','A','A','A'};
	int rank[5] = {1,1,1,1,1};
	
	for(i=0;i<5;i++){
		tot[i] = edps[i]+oa[i]+pg[i];
		avg[i] = (float) tot[i] / 3;
		if(avg[i]>=90) {
			hak[i] = 'A';
		} else if(avg[i]>=80) {
			hak[i] = 'B';
		} else if(avg[i]>=70) {
			hak[i] = 'C';
		} else if(avg[i]>=60) {
			hak[i] = 'D';
		} else {
			hak[i] = 'F';
		}
	} 
	for(i=0;i<5;i++){
		for(j=0;j<5;j++){
			if(tot[i] < tot[j]){
				rank[i]++;
			}
		}
	}
	
	printf("\n번호\tEDPS\tOA\tPG\t총점\t평균\t학점\t석차");
	for(i=0;i<5;i++){
		printf("\n%d\t%d\t%d\t%d\t%d\t%.2f\t%c\t%d",num[i],
		edps[i],oa[i],pg[i],tot[i],avg[i],hak[i],rank[i]);
	}
	
	return 0;
} 
