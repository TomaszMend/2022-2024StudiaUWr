#include <iostream>

using namespace std;

int main(){
	for(int i=41;i<48;i++){
		cout << "\x1b[" << i << "m" << endl;
		cout<<i;
		cout<<endl;
	}
	cout << "\x1b[40m" << endl;
	return 0;
}
