//���Ǻб⹮ : ���ǿ� ���� ó������� ���������� ���� - if, switch
#include <stdio.h>
int main(void){ //if, if~else, if~else if~else~, ��øif 
	int a = 10;
	int b = 20;
	if(a>b){
		printf("a�� �� Ů�ϴ�. %d", a);
	} else {
		printf("b�� �� Ů�ϴ�. %d", b);
	}
	
	int score = 90;	//���� 100~90:A, 89~80:B, 79~70:C, 69~60:D, 59~:F -> if~elseif~Ȱ�� 
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
	printf("\n����� ������ %c�Դϴ�.", hak);
	
	//���� ���ϱ� - ������ ��ҹ��ڿ� ������� A�̸� 5, B�̸� 4, C�̸� 3, D�̸� 2,
	//F�̸� 1�� ���� - switch~case Ȱ��
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
	printf("\n����� ������ %d�����Դϴ�.",point);
	return 0;
} 

