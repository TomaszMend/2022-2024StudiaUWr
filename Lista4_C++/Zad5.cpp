#include <iostream>
using namespace std;
int main(){
	int limit;
	cout<<"Wyznacz limit argumentów dla ciągu Fibonacciego"<<endl;
	cin>>limit;
	int f[limit];
	for(int i=0;i<limit;i++){
		f[i]=f[i-1]+f[i-2];
		if(i==0){
			f[i]=0;
		}
		if(i==1){
			f[i]=1;
		}
		cout<<f[i]<<endl;
	}
	return 0;
}

