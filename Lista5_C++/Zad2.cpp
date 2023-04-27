#include <iostream>
#include <cmath>
#include <ctime>
using namespace std;

void Zamiana(int rozmiar, int tab[]){
	int zapas;
	int roz=rozmiar/2;
	int roz_zapas=rozmiar;
	for(int i=0;i<roz;i++){
		roz_zapas--;
		zapas=tab[i];
		tab[i]=tab[roz_zapas];
		tab[roz_zapas]=zapas;
	}
	for(int i=0; i<rozmiar; i++){
		cout<<tab[i]<<"\t";
	}
	cout<<endl;
}
int main(){
	srand(time(NULL));
	cout<<"Ile argumentów ma mieć tablica? (argumenty będą losowe od 0 do 100)"<<endl;
	int n;
	cin>>n;
	int tab[n];
	for(int i=0;i<n;i++){
		tab[i]=rand()%101;
		cout<<tab[i]<<"\t";
	}
	cout<<endl;
	Zamiana(n,tab);
	return 0;
}
