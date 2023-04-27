#include <SFML/Window.hpp>
#include <SFML/Graphics.hpp>
#include <stdio.h>
#include <time.h> 

int main() {
	int const rozx=1080;
	int const rozy=750;
	int const R=100;
	float const g=9.81;
	int const N=10;
	sf::CircleShape kola[N];
	int keyonoff = 1;
	float x=200,y=200;
	for(int i=0; i<N;i++){
		kola[i]= sf::CircleShape(R*(rand()/(float)RAND_MAX));
		kola[i].setPosition(rozx/2*(rand()/(float)(RAND_MAX)),rozy/2*(rand()/(float)(RAND_MAX)));
		kola[i].setFillColor(sf::Color::Green);
	}
    	float vx=0.01, vy=0;
    	float timer=time(NULL);
    	sf::Clock zegar;
    	//sf::Clock deltaClock;
	sf::RenderWindow window(sf::VideoMode(rozx,rozy), "Nasze okno");
	//sf::CircleShape shape(R);
	//shape.setPosition(x,y);
	//shape.setFillColor(sf::Color::Green);
	while (window.isOpen()) {
		int dt=time(NULL)-timer;
		for(int i=0;i<N;i++){
			kola[i].move(vx,vy);
		}
                //x=x+vx*dt;
                //y=y+vy*dt;
                vy=vy+g*dt;
                timer=time(NULL);
		for(int i=0;i<N;i++){
		int pozx = kola[i].getPosition().x;
		int pozy = kola[i].getPosition().y;
		if(pozx>=rozx-(R*2) || pozx<=0){
			vx=-vx;
		}
		if(pozy>=rozy-(R*2) || pozy<=0){
			vy=-vy;
		}
		}
		sf::Event event;
		while (window.pollEvent(event)) {
			if (event.type == sf::Event::Closed)
				window.close();
			if (event.type == sf::Event::KeyPressed)
				keyonoff = 1 - keyonoff;
			if(event.key.code == sf::Keyboard::Escape)
				window.close();
		}
		window.clear(sf::Color::Black);
		for(int i=0;i<N;i++)
			window.draw(kola[i]);
		window.display();
	}
	return 0;
}
