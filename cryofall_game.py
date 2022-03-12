import math  
import cv2 as cv
import numpy as np
import os
import pyautogui
from time import time
from time import sleep
from time import *
from cryofallScreenCapture import cryofallScreenCapture
from prime import Prime
import random

os.chdir(os.path.dirname(os.path.abspath(__file__)))
# Image Loop
# cryofallScreenCapture.list_window_names()
wincap = cryofallScreenCapture('CryoFall')
Prime_resources = Prime('find_stone.png')
time_loop = time()
while(True):
    pyautogui.FAILSAFE = True
    screenshot = wincap.capture_screenshot()
    # cv.imshow('Computer Vision', screenshot)
    points = Prime_resources.findClickPositions(screenshot, 0.69, 'rectangles')
    # print("This are the Points:", points)
    # The midpoit of the x axis width window
    sleep(5)
    window = pyautogui.size()
    window_x = window[0]
    window_y = window[1]
    x_axis = window_x
    first_x_mid_point = x_axis / 2
    second_x_mid_point = first_x_mid_point + 1

    # Getting the mid_point of the y axis height window
    y_axis = window_y
    first_y_mid_point = y_axis / 2
    second_y_mid_point = first_y_mid_point + 1

    # Assigning the time take on half of the screen to the other side.
    time_taken_x_axis = 6
    time_taken_y_axis = 3.5
    resource_position = points[0]

    x_cordinates = resource_position[0]
    y_cordinates = resource_position[1]
    # top left side x axis
    left_side_less_x = first_x_mid_point - x_cordinates
    algorithm_calc_x = left_side_less_x * time_taken_x_axis
    time_in_second_x = algorithm_calc_x /  first_x_mid_point
    # top left y axis
    left_side_less_y = first_y_mid_point - y_cordinates
    algorithm_calc_y = left_side_less_y * time_taken_y_axis
    time_in_second_y = algorithm_calc_y / first_y_mid_point
    # top right side x axis
    right_side_more_x =  x_cordinates - first_x_mid_point 
    algorithm_calc_x_right = right_side_more_x * time_taken_x_axis
    time_in_second_x_right = algorithm_calc_x_right /  first_x_mid_point
    # bottom right side y axis
    right_side_more_y =  y_cordinates - first_y_mid_point   
    algorithm_calc_y_right = right_side_more_y * time_taken_y_axis
    time_in_second_y_right = algorithm_calc_y_right /  first_y_mid_point
    print(points)
    pyautogui.click(x=682, y=399)

    if x_cordinates <= int(first_x_mid_point) and y_cordinates <= int(first_y_mid_point):
        pyautogui.keyDown('a')
        sleep(round(time_in_second_x, 1))
        pyautogui.keyUp('a')
        sleep(0.1)
        pyautogui.keyDown('w')
        sleep(time_in_second_y)
        pyautogui.keyUp('w')
        sleep(0.1)

        pyautogui.keyDown('i')
        sleep(1)
        pyautogui.keyUp('i')

    if x_cordinates <= int(first_x_mid_point) and y_cordinates >= int(first_y_mid_point):
        pyautogui.keyDown('a')
        sleep(round(time_in_second_x, 1))
        pyautogui.keyUp('a')
        sleep(0.1)
        pyautogui.keyDown('s')
        sleep(time_in_second_y_right)
        pyautogui.keyUp('s')
        sleep(0.1)

        pyautogui.keyDown('i')
        sleep(1)
        pyautogui.keyUp('i')

    if x_cordinates >= int(second_x_mid_point) and y_cordinates <= int(second_y_mid_point):
        pyautogui.keyDown('d')
        sleep(round(time_in_second_y, 1))
        pyautogui.keyUp('d')
        sleep(0.1)
        pyautogui.keyDown('w')
        sleep(time_in_second_y)
        pyautogui.keyUp('w')
        sleep(0.1)

        pyautogui.keyDown('i')
        sleep(1)
        pyautogui.keyUp('i')

    if x_cordinates >= int(second_x_mid_point) and y_cordinates >= int(second_y_mid_point):
        pyautogui.keyDown('d')
        sleep(round(time_in_second_x_right, 1))
        pyautogui.keyUp('d')
        sleep(0.1)
        pyautogui.keyDown('s')
        sleep(time_in_second_y_right)
        pyautogui.keyUp('s')
        sleep(0.1)

        pyautogui.keyDown('i')
        sleep(1)
        pyautogui.keyUp('i')

    # Listing and Checking the closest points to the player
    print("The cordinates information", x_cordinates, y_cordinates)
    
    time_loop = time()

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
    print("done")

capture_window()
                # print('Done.')





# install the following packages
# sudo apt-get install scrot
# sudo apt-get install python3-tk python3-dev