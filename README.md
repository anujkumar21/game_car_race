<p align="center">
  <img src="./img/Car_Race.jpg" />
</p>

# Car Race Game Like Gym
This game can be controlled by another program or by a keyboard.

## Prerequisites

### Python and Libraries
* Python v3.9.6
* Pygame v2.0.1

## How to play using keyboard
You can run "main.py" and play using the following keys:
* Left arrow
* Right arrow
* ESC - To close the game

## How to play using another program
To import and send commands to the game, you can uso the following code:
````
from Car_Race_Game_Like_Gym.car_race import CarRacing
car_racing = CarRacing(keyboard_game=False, increase_speed=1, low_enemy_car_speed=5, max_enemy_car_speed=11)
car_racing.start()
while True:
    car_racing.step(0) # Use the action
````
In the parameter of "car_racing.step()" you pass the action you want to perform in the game.

### Actions
Actions you can send to the program:
* 0 - Left lane
* 1 - Middle lane
* 2 - Right lane

## Customizations
When start the game you can do some customizations listed below:
* **keyboard_game** - Play using keyboard or sending commands (by another program)
* **increase_speed** - How much speed will increase every 100 points
* **low_speed** - Minimum speed allowed (when starting the game)
* **max_speed** - Maximum speed allowed

## Authors

### Created by
* **Anuj Kumar** - [anujkumar21](https://github.com/anujkumar21)

### Changed by

* **Maxwell F. Barbosa** - [MaxwellFB](https://github.com/MaxwellFB)
