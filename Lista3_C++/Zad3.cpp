#include <iostream>
using namespace std;
int main(){
  bool dziala=false;
  int zapas;
  int n=0;
  do{
	int silnia=1;
	  for(int i=1; i<n+1;i++){
	  	zapas=silnia;
	  	silnia=silnia*i;
	  }
	  cout<<"N: "<<n<<endl;
	cout<<"Silnia od N: "<<silnia<<endl;
	if(zapas>silnia){
	  break;
	}
	n++;
	if(silnia<0){
	  cout<<"Break nie zadziałał"<<endl;
	}
  }while(dziala==false);
  cout<<"Najwyzsza liczba mozliwa dla n jest rowna "<<n-1<<endl;
  cout<<zapas<<endl;
  return 0;
}
