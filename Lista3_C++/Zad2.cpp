#include <iostream>
#include <unistd.h>
using namespace std;

int main(){
	while(1>0){
	   system("clear");
	   srand(time(0));
	   for(int i=0;i<50;i++){
		for(int j=0;j<210;j++){
			int x=(rand() % 230) + 1;
			cout << "\x1b["<< x <<"m"<<(rand() % 10) + 1;
		}
		cout << "\x1b[98m" << endl;
	   }
	   sleep(1);
	}
	return 0;
}
