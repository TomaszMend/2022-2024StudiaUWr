#include <iostream>
using namespace std;
int main(){
	int limit;
	cout<<"Wyznacz limit argumentów dla ciągu mojego"<<endl;
	cin>>limit;
	int f[limit];
	for(int i=1;i<limit+1;i++){
		f[i]=f[i-1]*i;
		if(i==1){
			f[i]=1;
		}
		cout<<f[i]<<endl;
	}
	return 0;
}

