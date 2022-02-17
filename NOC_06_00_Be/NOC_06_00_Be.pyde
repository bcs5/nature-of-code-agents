# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Modified by Filipe Calegario

# Draws a "vehicle" on the screen

from Vehicle import Vehicle
from Food import Food

def setup():
    global vehicle, food
    size(640, 360)
    velocity = PVector(0.0, 0.0)
    vehicle = Vehicle(width / 2, height / 2, velocity)
    food = Food(25)

def draw():
    background(51)
    mouse = PVector(mouseX, mouseY)
    target = food.position
    vehicle.arrive(target)
    vehicle.update()
    food.update(vehicle.position)
    vehicle.display()
    food.display()
