#include <iostream>

using namespace std;

int main(){
	int x=-5;
	int y=-5;
	for(int i=0;i<11;i++){
		cout<<"\t ["<<x<<"]";
		x++;
	}
	cout<<endl;
	x=-5;
	for(int i=0; i<11;i++){
		cout<<"["<<x<<"]";
		y=-5;
		for(int j=0;j<11;j++){
			cout<<"\t"<<x*y;
			y++;
		}
		cout<<endl;
		x++;
	}
	return 0;
}
