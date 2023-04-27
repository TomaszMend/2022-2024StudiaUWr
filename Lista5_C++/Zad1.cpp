#include <iostream>

using namespace std;
int readMass(){
	int weight;
	cout<<"Wpisz wagę w kilogramach"<<endl;
	cin>> weight;
	return weight;
}
float readHeight(){
	float height;
	cout<<"Wpisz wzrost w metrach"<<endl;
	cin>> height;
	return height;
}
float BMI(float h, int w){
	return w/h/h;
}
void BMIprint( float BMIn )
{
//	cout<<BMIn<<endl;
    if( BMIn < 18 )
         cout << "Masz niedowagę " << endl;
    if( BMIn >= 18 && BMIn <= 25 )
         cout << "Waga prawidłowa " << endl;
    if( BMIn > 25 )
         cout << "Masz nadwagę " << endl;
   
}
int main(){
	int weight=0;
	float height=0, BMIn=0;
	BMIprint(BMI(readHeight(), readMass()));

}
