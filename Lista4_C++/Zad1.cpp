#include <iostream>
using namespace std;

void funkcjaA(){
	cout<<"Hello World"<<endl;
}
void funkcjaB(){
	float a;
	cin>>a;
	cout<<a<<endl;
}
void funkcjaC(){
	cout<<"Wpisz int A"<<endl;
	int a;
	cin>>a;
	cout<<"Wpisz int B"<<endl;
	int b;
	cin>>b;
	cout<<"Wychodzi int C:"<<endl;
	int c;
	c=a+b;
	cout<<c<<endl;
}
void funkcjaD(){
	cout<<"Wpisz int A"<<endl;
	int a;
	cin>>a;
	cout<<"Wpisz float B"<<endl;
	float b;
	cin>>b;
	cout<<"Wpisz float C"<<endl;
	float c;
	cin>>c;
	cout<<"Wychodzi int D:"<<endl;
	int d;
	d=a*b*c;
	cout<<d<<endl;
}
void funkcjaE(int x){
	int t[x];
	int mno=1;
	for(int i=1;i<x+1;i++){
		mno=mno*i;
	}
	cout<<mno<<endl;
}

int main(){

cout<<endl<<"A"<<endl;
funkcjaA();
cout<<endl<<"B"<<endl;
funkcjaB();
cout<<endl<<"C"<<endl;
funkcjaC();
cout<<endl<<"D"<<endl;
funkcjaD();
cout<<endl<<"E"<<endl;
int x;
cout<<"Podaj wymiar tablicy"<<endl;
cin>>x;
funkcjaE(x);
return 0;
}
