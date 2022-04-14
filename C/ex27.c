//4. 5���� ����, OA, PG�� ������ ��ȣ�� �迭�� �Է¹޾� �ش� �л����� 
//��������, ���� ���, ����, ������ ����Ͽ� ����ϴ� ���α׷��� �ۼ� �϶�
//��, ������ ���� ������ ���� ū ����� ������ 1���̸�, ������ 90���̻�(A), 
//80~89��(B), 70~79��(C), 60~69��(D) �������� F�� �Ѵ�.
//���� ���� = ����(EDPS)����+OA����+PG����
//���� ��� = ���� ���� / �����
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
	
	printf("\n��ȣ\tEDPS\tOA\tPG\t����\t���\t����\t����");
	for(i=0;i<5;i++){
		printf("\n%d\t%d\t%d\t%d\t%d\t%.2f\t%c\t%d",num[i],
		edps[i],oa[i],pg[i],tot[i],avg[i],hak[i],rank[i]);
	}
	
	return 0;
} 
