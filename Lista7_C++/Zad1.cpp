#include <SFML/Window.hpp>
#include <SFML/Graphics.hpp>
#include <stdio.h>
#include <time.h> 
int main() {
	int keyonoff = 1;
	float x=200,y=200;
	const int roz=800;
	float timer=time(NULL);
	sf::RenderWindow window(sf::VideoMode(roz, roz), "Nasze okno");
	sf::CircleShape shape(200);
	shape.setPosition(x,y);
	shape.setFillColor(sf::Color::Red);
	while (window.isOpen()) {
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
		if (keyonoff)
			window.draw(shape);
		window.display();
	}
	return 0;
}
