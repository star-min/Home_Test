#include <iostream>
#include <malloc.h>
using namespace std;
void main()
{
	int** score;
	int studentNum = 0;
	int lessonNum = 0;
	int allTotalSize = 0;
	cout << "학생 수 입력 :";
	cin >> studentNum;
	score = new int*[studentNum];
	
	cout << "sizefo(score):"<< sizeof(score) <<"byte"<<endl;
	cout << "_msize(score):"<< _msize(score) << "byte" << endl << endl;
		allTotalSize = _msize(score);
	for(int i=0;i<studentNum;i++)
	{
		cout << (i+1)<<"번 학생의 수강 과목 수:";
		cin >> lessonNum;
		score[i] = new int[lessonNum];
		allTotalSize += _msize(score[i]);
		cout << (i+1) << "번째 배열의 크기:"<< _msize(score[i])<<"byte"<<endl<<endl;
		
	}
	cout<< endl << "2차워 포인터 배열 전체의 크기 :"<< allTotalSize << "byte"<<endl;
	delete score;
}
