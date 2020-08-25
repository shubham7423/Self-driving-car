#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 11:30:26 2020

@author: shubhampatel
"""




import numpy as np



from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Line, InstructionGroup
from kivy.config import Config
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock



from ai import Dqn


Config.set('input', 'mouse', 'mouse,multitouch_on_demand')


last_x = 0
last_y = 0
n_points = 0
length = 0


brain_1 = Dqn(5,3,0.9)
brain_2 = Dqn(5,3,0.9)
action2rotation = [0,20,-20]
last_reward_1 = 0
last_reward_2 = 0
scores_1 = []
scores_2 = []

# init map
first_update = True
def init():
    global sand
    global goal_x_1
    global goal_y_1
    global goal_x_2
    global goal_y_2
    global first_update
    sand = np.zeros((longueur,largeur))
    
#    middle line
    for x in range(0, 1600):
            sand[x, 600] = 1
            sand[x, 601] = 1
        
#    bottom line
    for x in range(0, 1600):
            sand[x, 398] = 1
            sand[x, 399] = 1
            sand[x, 400] = 1
            sand[x, 401] = 1
            sand[x, 402] = 1
            
#    upper line
    for x in range(0, 1600):
            sand[x, 798] = 1
            sand[x, 799] = 1
            sand[x, 800] = 1
            sand[x, 801] = 1
            sand[x, 802] = 1
            
    goal_x_1 = 20
    goal_y_1 = (largeur)/2 + 100
    goal_x_2 = longueur - 20
    goal_y_2 = (largeur)/2 - 100
    
    first_update = False

# Initializing the last distance
last_distance_1 = 0
last_distance_2 = 0

# Creating the car class

class Car_1(Widget):
    
    angle = NumericProperty(0)
    rotation = NumericProperty(0)
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    sensor1_x = NumericProperty(0)
    sensor1_y = NumericProperty(0)
    sensor1 = ReferenceListProperty(sensor1_x, sensor1_y)
    sensor2_x = NumericProperty(0)
    sensor2_y = NumericProperty(0)
    sensor2 = ReferenceListProperty(sensor2_x, sensor2_y)
    sensor3_x = NumericProperty(0)
    sensor3_y = NumericProperty(0)
    sensor3 = ReferenceListProperty(sensor3_x, sensor3_y)
    signal1 = NumericProperty(0)
    signal2 = NumericProperty(0)
    signal3 = NumericProperty(0)

    def move(self, rotation):
        self.pos = Vector(*self.velocity) + self.pos
        self.rotation = rotation
        self.angle = self.angle + self.rotation
        self.sensor1 = Vector(30, 0).rotate(self.angle) + self.pos
        self.sensor2 = Vector(30, 0).rotate((self.angle+30)%360) + self.pos
        self.sensor3 = Vector(30, 0).rotate((self.angle-30)%360) + self.pos
        self.signal1 = int(np.sum(sand[int(self.sensor1_x)-10:int(self.sensor1_x)+10, int(self.sensor1_y)-10:int(self.sensor1_y)+10]))/400.
        self.signal2 = int(np.sum(sand[int(self.sensor2_x)-10:int(self.sensor2_x)+10, int(self.sensor2_y)-10:int(self.sensor2_y)+10]))/400.
        self.signal3 = int(np.sum(sand[int(self.sensor3_x)-10:int(self.sensor3_x)+10, int(self.sensor3_y)-10:int(self.sensor3_y)+10]))/400.
        if self.sensor1_x>longueur-10 or self.sensor1_x<10 or self.sensor1_y>largeur-10 or self.sensor1_y<10:
            self.signal1 = 1.
        if self.sensor2_x>longueur-10 or self.sensor2_x<10 or self.sensor2_y>largeur-10 or self.sensor2_y<10:
            self.signal2 = 1.
        if self.sensor3_x>longueur-10 or self.sensor3_x<10 or self.sensor3_y>largeur-10 or self.sensor3_y<10:
            self.signal3 = 1.

class Ball1_1(Widget):
    pass
class Ball2_1(Widget):
    pass
class Ball3_1(Widget):
    pass

class Car_2(Widget):
    angle = NumericProperty(0)
    rotation = NumericProperty(0)
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    sensor1_x = NumericProperty(0)
    sensor1_y = NumericProperty(0)
    sensor1 = ReferenceListProperty(sensor1_x, sensor1_y)
    sensor2_x = NumericProperty(0)
    sensor2_y = NumericProperty(0)
    sensor2 = ReferenceListProperty(sensor2_x, sensor2_y)
    sensor3_x = NumericProperty(0)
    sensor3_y = NumericProperty(0)
    sensor3 = ReferenceListProperty(sensor3_x, sensor3_y)
    signal1 = NumericProperty(0)
    signal2 = NumericProperty(0)
    signal3 = NumericProperty(0)

    def move(self, rotation):
        self.pos = Vector(*self.velocity) + self.pos
        self.rotation = rotation
        self.angle = self.angle + self.rotation
        self.sensor1 = Vector(30, 0).rotate(self.angle) + self.pos
        self.sensor2 = Vector(30, 0).rotate((self.angle+30)%360) + self.pos
        self.sensor3 = Vector(30, 0).rotate((self.angle-30)%360) + self.pos
        self.signal1 = int(np.sum(sand[int(self.sensor1_x)-10:int(self.sensor1_x)+10, int(self.sensor1_y)-10:int(self.sensor1_y)+10]))/400.
        self.signal2 = int(np.sum(sand[int(self.sensor2_x)-10:int(self.sensor2_x)+10, int(self.sensor2_y)-10:int(self.sensor2_y)+10]))/400.
        self.signal3 = int(np.sum(sand[int(self.sensor3_x)-10:int(self.sensor3_x)+10, int(self.sensor3_y)-10:int(self.sensor3_y)+10]))/400.
        if self.sensor1_x>longueur-10 or self.sensor1_x<10 or self.sensor1_y>largeur-10 or self.sensor1_y<10:
            self.signal1 = 1.
        if self.sensor2_x>longueur-10 or self.sensor2_x<10 or self.sensor2_y>largeur-10 or self.sensor2_y<10:
            self.signal2 = 1.
        if self.sensor3_x>longueur-10 or self.sensor3_x<10 or self.sensor3_y>largeur-10 or self.sensor3_y<10:
            self.signal3 = 1.
            
class Ball1_2(Widget):
    pass
class Ball2_2(Widget):
    pass
class Ball3_2(Widget):
    pass

# Creating the game class

class Game(Widget):

    car_1 = ObjectProperty(None)
    ball1_1 = ObjectProperty(None)
    ball2_1 = ObjectProperty(None)
    ball3_1 = ObjectProperty(None)
    
    car_2 = ObjectProperty(None)
    ball1_2 = ObjectProperty(None)
    ball2_2 = ObjectProperty(None)
    ball3_2 = ObjectProperty(None)

    def serve_car(self):
        self.car_1.center = self.center
        self.car_1.velocity = Vector(6, 0)
        
        self.car_2.center = self.center
        self.car_2.velocity = Vector(6, 0)

    def update(self, dt):

        global brain_1
        global brain_2
        global last_reward_1
        global last_reward_2
        global scores_1
        global scores_2
        global last_distance_1
        global last_distance_2
        global goal_x_1
        global goal_y_1
        global goal_x_2
        global goal_y_2
        global longueur
        global largeur

        longueur = self.width
        largeur = self.height
        if first_update:
            init()

        xx_1 = goal_x_1 - self.car_1.x
        yy_1 = goal_y_1 - self.car_1.y
        orientation_1 = Vector(*self.car_1.velocity).angle((xx_1,yy_1))/180.
        last_signal_1 = [self.car_1.signal1, self.car_1.signal2, self.car_1.signal3, orientation_1, -orientation_1]
        action_1 = brain_1.update(last_reward_1, last_signal_1)
        scores_1.append(brain_1.score())
        rotation = action2rotation[action_1]
        self.car_1.move(rotation)
        distance_1 = np.sqrt((self.car_1.x - goal_x_1)**2 + (self.car_1.y - goal_y_1)**2)
        self.ball1_1.pos = self.car_1.sensor1
        self.ball2_1.pos = self.car_1.sensor2
        self.ball3_1.pos = self.car_1.sensor3

        if sand[int(self.car_1.x),int(self.car_1.y)] > 0:
            self.car_1.velocity = Vector(1, 0).rotate(self.car_1.angle)
            last_reward_1 = -1.5
            print("Car1: ", self.car_1.velocity)
        else: # otherwise
            self.car_1.velocity = Vector(6, 0).rotate(self.car_1.angle)
            last_reward_1 = -1.2
            if distance_1 < last_distance_1:
                last_reward_1 = 1.0

        if self.car_1.x < 10:
            self.car_1.x = 10
            last_reward_1 = -1.5
        if self.car_1.x > self.width - 10:
            self.car_1.x = self.width - 10
            last_reward_1 = -1
        if self.car_1.y < 10:
            self.car_1.y = 10
            last_reward_1 = -1
        if self.car_1.y > self.height - 10:
            self.car_1.y = self.height - 10
            last_reward_1 = -1

        if distance_1 < 100:
            goal_x_1 = self.width-goal_x_1
#            goal_y_1 = self.height-goal_y_1
        last_distance_1 = distance_1
        print("Car1: ", brain_1.score())
        
        #2nd car
        xx_2 = goal_x_2 - self.car_2.x
        yy_2 = goal_y_2 - self.car_2.y
        orientation_2 = Vector(*self.car_2.velocity).angle((xx_2,yy_2))/180.
        last_signal_2 = [self.car_2.signal1, self.car_2.signal2, self.car_2.signal3, orientation_2, -orientation_2]
        action_2 = brain_2.update(last_reward_2, last_signal_2)
        scores_2.append(brain_2.score())
        rotation = action2rotation[action_2]
        self.car_2.move(rotation)
        distance_2 = np.sqrt((self.car_2.x - goal_x_2)**2 + (self.car_2.y - goal_y_2)**2)
        self.ball1_2.pos = self.car_2.sensor1
        self.ball2_2.pos = self.car_2.sensor2
        self.ball3_2.pos = self.car_2.sensor3

        if sand[int(self.car_2.x),int(self.car_2.y)] > 0:
            self.car_2.velocity = Vector(1, 0).rotate(self.car_2.angle)
            last_reward_2 = -1.5
#            print("Car2: ", self.car_2.velocity)
        else: # otherwise
            self.car_2.velocity = Vector(6, 0).rotate(self.car_2.angle)
            last_reward_2 = -1.2
            if distance_2 < last_distance_2:
                last_reward_2 = 1.0

        if self.car_2.x < 10:
            self.car_2.x = 10
            last_reward_2 = -1
        if self.car_2.x > self.width - 10:
            self.car_2.x = self.width - 10
            last_reward_2 = -1
        if self.car_2.y < 10:
            self.car_2.y = 10
            last_reward_2 = -1
        if self.car_2.y > self.height - 10:
            self.car_2.y = self.height - 10
            last_reward_2 = -1

        if distance_2 < 100:
            goal_x_2 = self.width-goal_x_2
#            goal_y_2 = self.height-goal_y_2
        last_distance_2 = distance_2
#        print("Car2: ", last_reward_2)
        

# Adding the painting tools

class MyPaintWidget(Widget):
    
    def __init__(self, **kwargs):
        super(MyPaintWidget, self).__init__(**kwargs)
        global sand
        self.ig = InstructionGroup()
#        center line
        self.m_line = Line(points=[0, 600, 1600, 600], width=2)
        self.ig.add(self.m_line)
        

#        bottom line
        self.b_line = Line(points=[0, 400, 1600, 400], width=5)        
        self.ig.add(self.b_line) 
        
        
#        upper line
        self.u_line = Line(points=[0, 800, 1600, 800], width=5)        
        self.ig.add(self.u_line) 
        
           
        
        self.canvas.add(self.ig)

#        Thread(target=self.draw).start()

    def on_touch_down(self, touch):
        global length, n_points, last_x, last_y
        with self.canvas:
            Color(0.8,0.7,0)
            d = 10.
            touch.ud['line'] = Line(points = (touch.x, touch.y), width = 10)
            last_x = int(touch.x)
            last_y = int(touch.y)
            n_points = 0
            length = 0
            sand[int(touch.x),int(touch.y)] = 1

    def on_touch_move(self, touch):
        global length, n_points, last_x, last_y
        if touch.button == 'left':
            touch.ud['line'].points += [touch.x, touch.y]
            x = int(touch.x)
            y = int(touch.y)
            length += np.sqrt(max((x - last_x)**2 + (y - last_y)**2, 2))
            n_points += 1.
            density = n_points/(length)
            touch.ud['line'].width = int(20 * density + 1)
            sand[int(touch.x) - 10 : int(touch.x) + 10, int(touch.y) - 10 : int(touch.y) + 10] = 1
            last_x = x
            last_y = y

# Adding the API Buttons (clear, save and load)

class CarApp(App):

    def build(self):
        parent = Game()
        parent.serve_car()
        Clock.schedule_interval(parent.update, 1.0/60.0)
#        with self.canvas:
#            Line(points=[100, 100, 200, 100, 100, 200], width=10)
        self.painter = MyPaintWidget()
        clearbtn = Button(text = 'clear')
        savebtn = Button(text = 'save', pos = (parent.width, 0))
        loadbtn = Button(text = 'load', pos = (2 * parent.width, 0))
        clearbtn.bind(on_release = self.clear_canvas)
        savebtn.bind(on_release = self.save)
        loadbtn.bind(on_release = self.load)
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        parent.add_widget(savebtn)
        parent.add_widget(loadbtn)
        return parent

    def clear_canvas(self, obj):
        global sand
        self.painter.canvas.clear()
        sand = np.zeros((longueur,largeur))

    def save(self, obj):
        print("saving brain...")
        brain_1.save("last_brain_c1.pth")
        brain_2.save("last_brain_c2.pth")
        


    def load(self, obj):
        print("loading last saved brain...")
        brain_1.load("last_brain_c1.pth")
        brain_2.load("last_brain_c2.pth")


if __name__ == '__main__':
    CarApp().run()
    



