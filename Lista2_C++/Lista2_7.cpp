#include <iostream>
#include <cmath>
using namespace std;

int main(){
	for(float x=0; x<2*M_PI; x=x+0.01){
		cout<<x<<"\t"<<cos(x)<<endl;
	}
	return 0;
}
