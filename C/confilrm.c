//	5���� ����, OA, PG�� ������ ��ȣ�� �迭�� �Է¹޾� �ش� �л�����
//	��������, �������, ����, ���� �� ����Ͽ� ����ϴ� ���α׷��� �ۼ��϶�'
//	��,������ ���� ������ ���� ū ����� ������ 1���̸�, ������ 90�� �̻�(a)
//	80~89(b),70~79(c),60~69(d) ������ f
//	�������� �������� +oa���� + pg����
//	������� = ���� ���� / �����

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
	
	// ������� , ���� ���� 
	for(i=0;i<5;i++){
		tot[i] = ps[i]+oa[i]+pg[i];
		avg[i] = (float) tot[i]/3;
	}
	// �� �� 
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
	// ���� 
	for(i=0;i<5;i++){
		for(y=0;y<5;y++){
			if(tot[i]<tot[y]){
				suk[i]++;
			}
		}
	}
	//���
	printf("\n��ȣ\tPS\tOA\tPG\t����\t���\t����\t����");
	//for���� �̿��� ���
	for(i=0;i<5;i++){
		printf("\n%d\t%d\t%d\t%d\t%d\t%.2f\t%c\t%d",
		num[i],ps[i],oa[i],pg[i],tot[i],avg[i],hak[i],suk[i]);
	} 
	return 0;
}

