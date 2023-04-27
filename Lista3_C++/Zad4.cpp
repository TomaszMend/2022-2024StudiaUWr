#include <iostream>
using namespace std;
int main(){
	int t;
	int a,b;
	int p=2;

	while(p==2){
		cin.clear();
		cout<<"Wybierz opcje: 1-dodawanie, 2-mnozenie"<<endl;
		cin>>t;
		switch(t){
			case 1:
				cout<<"Wpisz pierwsza liczbe"<<endl;
				cin>>a;
				cout<<"Wpisz druga liczbe"<<endl;
				cin>>b;
				cout<<"Wynik:"<<endl;
				cout<<a+b<<endl;
				break;
			case 2:
				cout<<"Wpisz pierwsza liczbe"<<endl;
				cin>>a;
				cout<<"Wpisz druga liczbe"<<endl;
				cin>>b;
				cout<<"Wynik:"<<endl;
				cout<<a*b<<endl;
				break;
			}
		cin.clear();
		int spr=0;
		do{
			if(spr>0){
				cout<<"Niepoprawny wybór"<<endl;
			}
			spr++;
			cout<<"Czy chcialbys wykonac jeszcze jedno obliczenie? 1-nie 2-tak"<<endl;
			cin>>p;
			
		}while(p!=1 && p!=2);
	}
	return 0;
}
