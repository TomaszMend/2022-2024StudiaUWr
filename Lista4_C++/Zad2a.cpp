#include <iostream>
using namespace std;
int Wpisz(int N){
	do{
		cout<<"Wpisz N od 10 do 5000"<<endl;
		cin>>N;
		if( N>5000 || N<10){
			cout<<"Niepoprawna liczba"<<endl;
		}
	}while(N>5000 || N<10);
}
int Wyniki(int i, float suma, float srednia){
	srand(time(0));
	float x=rand() % 10;
	x=x/10;
	suma = suma+x;
	srednia = suma/i;
	cout<<suma<<"\t"<<srednia<<endl;
}
int main(){
	
	int N;
	Wpisz(N);
	float srednia=0;
	float suma=0;
	for(int i=1;i<N+1;i++){
		Wyniki(i,suma,srednia);
	}
	return 0;
}
