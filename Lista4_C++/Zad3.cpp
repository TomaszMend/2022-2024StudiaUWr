#include <iostream>
using namespace std;
int main(){
	srand(time(0));
	int x;
	cout<<"Od jakiej liczby ma być zakres:"<<endl;
	int a;
	cin>>a;
	int b;
	do{
	cout<<"Do jakiej liczby ma być zakres:"<<endl;
	cin>>b;
	if(b<a || b==a){
	cout<<"B nie może być mniejsze lub równe A"<<endl;
	}
	}while(b<a || b==a);
	x=rand() % b + a;
	for(int i=a;i<b+1;i++){
		cout<<i<<"\t";
	}
	int odp;
	cout<<endl;
	int lp=0;
	do{
		do{
		cout<<"Która liczbę wybierasz?"<<endl;
		cin>>odp;
		if(odp<a || odp>b){
			cout<<"Liczba nie jest nawet do wyboru, wybierz inną"<<endl;
		}
		}while(odp<a || odp>b);
		if(odp!=x){
		cout<<"Zła odpowiedz. Próbuj dalej."<<endl;
		lp++;
		}
	}while(odp!=x);
	cout<<"Udało Ci się podać dobrą odpowiedź!"<<endl<<"Błędne próby: "<<lp<<endl;

	return 0;
}
