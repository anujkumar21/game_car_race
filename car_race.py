""" 
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
@date: 29th-July-2018
"""
import random
from time import sleep

import pygame
import os


class CarRacing:
    def __init__(self, keyboard_game=True, increase_speed=1, low_enemy_car_speed=5, max_enemy_car_speed=11):

        pygame.init()
        self.display_width = 800
        self.display_height = 600
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.clock = pygame.time.Clock()
        self.gameDisplay = None
        self.root_path = os.path.dirname(os.path.realpath(__file__))

        self.keyboard_game = keyboard_game
        self.max_enemy_car_speed = max_enemy_car_speed
        self.low_enemy_car_speed = low_enemy_car_speed
        self.increase_speed = increase_speed

        self.quit_game = False

        self.reset()

    def reset(self):
        self.crashed = False

        self.carImg = pygame.image.load(self.root_path + "/img/car.png")
        self.car_x_coordinate = 310
        self.car_x_coordinate_available = [310, 375, 440]
        self.car_y_coordinate = (self.display_height * 0.8)
        self.car_width = 49

        # enemy_car
        self.enemy_car = pygame.image.load(self.root_path + "/img/enemy_car_1.png")
        self.enemy_car_startx = random.randrange(310, 450)
        self.enemy_car_starty = -600
        self.enemy_car_speed = self.low_enemy_car_speed
        self.enemy_car_width = 49
        self.enemy_car_height = 100

        # Background
        self.bgImg = pygame.image.load(self.root_path + "/img/back_ground.jpg")
        self.bg_x1 = (self.display_width / 2) - (360 / 2)
        self.bg_x2 = (self.display_width / 2) - (360 / 2)
        self.bg_y1 = 0
        self.bg_y2 = -600
        self.bg_speed = self.low_enemy_car_speed - 2
        self.count = 0

    def car(self, car_x_coordinate, car_y_coordinate):
        self.gameDisplay.blit(self.carImg, (car_x_coordinate, car_y_coordinate))

    def start(self):
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('Car Race -- Anuj')
        self.run_car()

    def run_car(self):
        if self.keyboard_game:
            while not self.quit_game:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.crashed = True
                    # print(event)

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.car_x_coordinate -= 65
                            # print ("CAR X COORDINATES: %s" % self.car_x_coordinate)
                        elif event.key == pygame.K_RIGHT:
                            self.car_x_coordinate += 65
                            # print ("CAR X COORDINATES: %s" % self.car_x_coordinate)
                        # print ("x: {x}, y: {y}".format(x=self.car_x_coordinate, y=self.car_y_coordinate))
                        elif event.key == pygame.K_ESCAPE:  # ESC
                            self.quit_game = True
                self.step()

    def step(self, action=None):
        """
        Move the car

        :param action: If keyboard_game=True the action is the position the car will be
        """
        if not self.keyboard_game:
            self.car_x_coordinate = self.car_x_coordinate_available[action]

        self.gameDisplay.fill(self.black)
        self.back_ground_road()

        self.run_enemy_car(self.enemy_car_startx, self.enemy_car_starty)
        self.enemy_car_starty += self.enemy_car_speed

        if self.enemy_car_starty > self.display_height:
            self.enemy_car_starty = 0 - self.enemy_car_height
            self.enemy_car_startx = random.randrange(310, 450)

        self.car(self.car_x_coordinate, self.car_y_coordinate)
        self.highscore(self.count)
        self.count += 1
        if self.count % 100 == 0 and self.enemy_car_speed < self.max_enemy_car_speed:
            self.enemy_car_speed += self.increase_speed
            self.bg_speed += self.increase_speed

        if self.car_y_coordinate < self.enemy_car_starty + self.enemy_car_height:
            if self.car_x_coordinate > self.enemy_car_startx and\
                    self.car_x_coordinate < self.enemy_car_startx + self.enemy_car_width or\
                    self.car_x_coordinate + self.car_width > self.enemy_car_startx and\
                    self.car_x_coordinate + self.car_width < self.enemy_car_startx + self.enemy_car_width:
                self.crashed = True
                self.display_message("Game Over !!!")

        if self.car_x_coordinate < 310 or self.car_x_coordinate > 460:
            self.crashed = True
            self.display_message("Game Over !!!")

        pygame.display.update()
        self.clock.tick(60)

    def display_message(self, msg):
        font = pygame.font.SysFont("comicsansms", 72, True)
        text = font.render(msg, True, (255, 255, 255))
        self.gameDisplay.blit(text, (400 - text.get_width() // 2, 240 - text.get_height() // 2))
        self.display_credit()
        pygame.display.update()
        self.clock.tick(60)
        sleep(1)
        self.reset()
        self.start()

    def back_ground_road(self):
        self.gameDisplay.blit(self.bgImg, (self.bg_x1, self.bg_y1))
        self.gameDisplay.blit(self.bgImg, (self.bg_x2, self.bg_y2))

        self.bg_y1 += self.bg_speed
        self.bg_y2 += self.bg_speed

        if self.bg_y1 >= self.display_height:
            self.bg_y1 = self.bg_y2 - 600

        if self.bg_y2 >= self.display_height:
            self.bg_y2 = self.bg_y1 - 600

    def run_enemy_car(self, thingx, thingy):
        self.gameDisplay.blit(self.enemy_car, (thingx, thingy))

    def highscore(self, count):
        font = pygame.font.SysFont("lucidaconsole", 20)
        text = font.render("Score : " + str(count), True, self.white)
        self.gameDisplay.blit(text, (0, 0))

    def display_credit(self):
        font = pygame.font.SysFont("lucidaconsole", 14)
        text = font.render("Thanks & Regards,", True, self.white)
        self.gameDisplay.blit(text, (600, 520))
        text = font.render("Anuj Kumar", True, self.white)
        self.gameDisplay.blit(text, (600, 540))
        text = font.render("cdac.anuj@gmail.com", True, self.white)
        self.gameDisplay.blit(text, (600, 560))

    def quit(self):
        pygame.quit()
        self.quit_game = True
