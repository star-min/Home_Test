//	5명의 전산, OA, PG의 점수와 번호를 배열로 입력받아 해당 학생들의
//	개인총점, 개인평균, 학점, 석차 를 계산하여 출력하는 프로그램을 작성하라'
//	단,석차는 개인 총점이 가장 큰 사람이 석차가 1등이며, 학점은 90점 이상(a)
//	80~89(b),70~79(c),60~69(d) 나머지 f
//	개인총점 전산점수 +oa점수 + pg점수
//	개인평균 = 개인 총점 / 과목수

# include<stdio.h>

int main(void){
	int i, y;
	int num[5] = {1,2,3,4,5};
	int ps[5] = {95,86,49,95,67};
	int oa[5] = {100,90,87,68,58};
	int pg[5] = {95,80,90,60,70};
	int tot[5] = {0,0,0,0,0};
	float avg[5] = {0.0,0.0,0.0,0.0,0.0};
	char hak[5] = {'A','A','A','A','A'};
	int suk[5] = {1,1,1,1,1};
	
	// 개인평균 , 개인 총점 
	for(i=0;i<5;i++){
		tot[i] = ps[i]+oa[i]+pg[i];
		avg[i] = (float) tot[i]/3;
	}
	// 학 점 
	for(i=0;i<5;i++){
		if(avg[i]>=90){
			hak[i] = 'A';
		} else if(avg[i]>=90) {
			hak[i] = 'B';
		} else if(avg[i]>=80){
			hak[i] = 'C';
		} else if(avg[i]>=70){
			hak[i] = 'D';
		} else if(avg[i]>=60){
			hak[i] = 'E';
		} else{
			hak[i] = 'F';
		}
	}
	// 석차 
	for(i=0;i<5;i++){
		for(y=0;y<5;y++){
			if(tot[i]<tot[y]){
				suk[i]++;
			}
		}
	}
	//출력
	printf("\n번호\tPS\tOA\tPG\t총점\t평균\t학점\t석차");
	//for문을 이용해 출력
	for(i=0;i<5;i++){
		printf("\n%d\t%d\t%d\t%d\t%d\t%.2f\t%c\t%d",
		num[i],ps[i],oa[i],pg[i],tot[i],avg[i],hak[i],suk[i]);
	} 
	return 0;
}

