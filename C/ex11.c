//조건분기문 : 조건에 따라 처리방법이 나누어지는 문장 - if, switch
#include <stdio.h>
int main(void){ //if, if~else, if~else if~else~, 중첩if 
	int a = 10;
	int b = 20;
	if(a>b){
		printf("a가 더 큽니다. %d", a);
	} else {
		printf("b가 더 큽니다. %d", b);
	}
	
	int score = 90;	//학점 100~90:A, 89~80:B, 79~70:C, 69~60:D, 59~:F -> if~elseif~활용 
	char hak;
	if(score>=90){
		hak = 'A';
	} else if(score>=80){
		hak = 'B';
	} else if(score>=70){
		hak = 'C';
	} else if(score>=60){
		hak = 'D';
	} else {
		hak = 'F';
	}
	printf("\n당신의 학점은 %c입니다.", hak);
	
	//평점 구하기 - 학점이 대소문자에 관계없이 A이면 5, B이면 4, C이면 3, D이면 2,
	//F이면 1로 구함 - switch~case 활용
	int point; 
	switch(hak){
		case 'a':
		case 'A':
			point = 5;
			break;
		case 'b':
		case 'B':
			point = 4;
			break;
		case 'c':
		case 'C':
			point = 3;
			break;
		case 'd':
		case 'D':
			point = 2;
			break;
		default:
			point = 1;
			break;
	} 
	printf("\n당신의 평점은 %d수준입니다.",point);
	return 0;
} 

