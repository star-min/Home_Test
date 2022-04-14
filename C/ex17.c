#include <stdio.h>
//배열(array) : 같은 이름, 타입의 데이터를 연속으로  저장할 수 자료구조 
//타입 배열명[요소수] = { 요소값0, 요소값1, 요소값2,...}; 
//타입 배열명[요소수];
//배열명[인덱스] = 요소값; 
//이름 -> name 
//한 사람의 과목점수인 국어, 영어, 수학, 과학, 사회을 저장할 수 있는 배열변수 -> score
//임의의 데이터를 각 과목에 입력하여 총점, 평균을 계산하여
//이름, 국어, 영어, 수학, 과학, 사회, 총점, 평균을 계산하여 출력하는 프로그램을 완성
int main(void){
	char name[4] = "kim";
	int score[5] = {90,80,85,75,90};
	int tot = 0;
	int i;
	for(i=0;i<5;i++){		tot+=score[i];	}
	//int tot = score[0]+score[1]+score[2]+score[3]+score[4];
	float avg = (float) tot / 5;
	printf("%s\t%d\t%d\t%d\t%d\t%d\t%d\t%.2f", name, score[0],score[1],score[2],
	score[3],score[4],tot,avg);
	return 0;
}
 
