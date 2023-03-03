from time import sleep
from pynput.mouse import Controller
mouse = Controller()
flip = 10
while True:
    #print('The current pointer position is {0}'.format(
    #mouse.position))
    print(".")
    mouse.move(1*flip, -1*flip)
    flip*=-1
    sleep(10)
