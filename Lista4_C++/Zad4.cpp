#include <iostream>
using namespace std;
int main(){
	cout<<"\x1b[40mWitaj w grze Zgadywanka!"<<endl;
	cout<<"Kliknij \x1b[41menter\x1b[40m na klawiaturze aby zacząć!"<<endl;
	cin.ignore();
	int p=0;
	int n=10;
	do{
		srand(time(0));
		int x;
		x=rand() % n;
		for(int i=1;i<n+1;i++){
			cout<<i<<"\t";
		}
		int odp;
		cout<<endl;
		int lp=0;
		do{
			do{
				cout<<"Która liczbę wybierasz?"<<endl;
				cin>>odp;
				if(odp<1 || odp>10){
					cout<<"Liczba nie jest nawet do wyboru, wybierz inną"<<endl;
				}
			}while(odp<1 || odp>10);
			
			if(odp!=x){
				cout<<"Zła odpowiedz. Próbuj dalej."<<endl;
				lp++;
			}
		}while(odp!=x);
		cout<<"Udało Ci się podać dobrą odpowiedź!"<<endl<<"Błędne próby: "<<lp<<endl;
		cout<<"Czy chcesz przejść do następnego poziomu? (Wpisz 1 jeżeli Tak, 0 jeżeli Nie)"<<endl;
		cin>>p;
		n++;
	}while(p==1);
	return 0;
}
