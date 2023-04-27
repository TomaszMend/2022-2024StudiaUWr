#include <iostream>
using namespace std;
int main(){
	srand(time(0));
	int N;
	do{
	cout<<"Wpisz N od 10 do 5000"<<endl;
	cin>>N;
	if( N>5000 || N<10){
		cout<<"Niepoprawna liczba"<<endl;
	}
	}while(N>5000 || N<10);
	float srednia=0;
	float suma=0;
	for(int i=1;i<N+1;i++){
		float x=rand() % 10;
		x=x/10;
		suma = suma+x;
		srednia = suma/i;
		cout<<suma<<"\t"<<srednia<<endl; 
	}
	return 0;
}
