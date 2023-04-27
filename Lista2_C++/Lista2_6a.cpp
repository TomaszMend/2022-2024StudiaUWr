#include <iostream>

using namespace std;

int main(){
	srand(time(0));
	for(int i=0;i<46;i++){
		for(int j=0;j<200;j++){
			int x=(rand() % 230) + 1;
			cout << "\x1b["<< x <<"m"<<(rand() % 10) + 1;
		}
	cout << "\x1b[98m" << endl;
	}
	return 0;
}
