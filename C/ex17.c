#include <stdio.h>
//�迭(array) : ���� �̸�, Ÿ���� �����͸� ��������  ������ �� �ڷᱸ�� 
//Ÿ�� �迭��[��Ҽ�] = { ��Ұ�0, ��Ұ�1, ��Ұ�2,...}; 
//Ÿ�� �迭��[��Ҽ�];
//�迭��[�ε���] = ��Ұ�; 
//�̸� -> name 
//�� ����� ���������� ����, ����, ����, ����, ��ȸ�� ������ �� �ִ� �迭���� -> score
//������ �����͸� �� ���� �Է��Ͽ� ����, ����� ����Ͽ�
//�̸�, ����, ����, ����, ����, ��ȸ, ����, ����� ����Ͽ� ����ϴ� ���α׷��� �ϼ�
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
 
