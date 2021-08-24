from car_race import CarRacing

def main():
    # if "keyboard_game=False", need to use "step(action)" to play
    car_racing = CarRacing(keyboard_game=True, increase_speed=1, low_enemy_car_speed=5, max_enemy_car_speed=11)
    car_racing.start()


if __name__ == '__main__':
    main()
