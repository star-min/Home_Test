#include <iostream>
#include <malloc.h>
using namespace std;
void main()
{
	int** score;
	int studentNum = 0;
	int lessonNum = 0;
	int allTotalSize = 0;
	cout << "�л� �� �Է� :";
	cin >> studentNum;
	score = new int*[studentNum];
	
	cout << "sizefo(score):"<< sizeof(score) <<"byte"<<endl;
	cout << "_msize(score):"<< _msize(score) << "byte" << endl << endl;
		allTotalSize = _msize(score);
	for(int i=0;i<studentNum;i++)
	{
		cout << (i+1)<<"�� �л��� ���� ���� ��:";
		cin >> lessonNum;
		score[i] = new int[lessonNum];
		allTotalSize += _msize(score[i]);
		cout << (i+1) << "��° �迭�� ũ��:"<< _msize(score[i])<<"byte"<<endl<<endl;
		
	}
	cout<< endl << "2���� ������ �迭 ��ü�� ũ�� :"<< allTotalSize << "byte"<<endl;
	delete score;
}
