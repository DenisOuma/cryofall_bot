import math 
import pyautogui
from time import *
from time import time
# print(pyautogui.size())
# pyautogui.click(x=682, y=399)
print(window)
window_x = window[0]
window_y = window[1]
print(window_x)
# direction = random.randint(0,4)
# test = [(600,80), (200, 60)]
# print(test[0])


# time_taken_x_axis = 6
# x_cordinates = 600
# mid_point = 683

# # calaculating the time in seconds taken to get to the point we want
# left_side_less = mid_point - x_cordinates
# algorithm_calc = left_side_less * time_taken_x_axis
# time_in_second = algorithm_calc /  mid_point
# print()


#  while direction > 0:
#         if direction == 0:
#             pyautogui.keyDown('a')
#             sleep(2)
#             pyautogui.keyDown('i')
#             sleep(4)
#             pyautogui.keyUp('i')

#         elif direction == 2:
#             pyautogui.keyUp('w')
#             sleep(2)
#             pyautogui.keyDown('i')
#             sleep(4)
#             pyautogui.keyUp('i')
#         elif direction == 3:
#             pyautogui.keyUp('d')
#             sleep(2)
#             pyautogui.keyDown('i')
#             sleep(4)
#             pyautogui.keyUp('i')
#         elif direction == 4:
#             pyautogui.keyUp('s')
#             sleep(2)
#             pyautogui.keyDown('i')
#             sleep(4)
#             pyautogui.keyUp('i')

#         break
# x_axis = 1366
# first_x_mid_point = x_axis / 2
# second_x_mid_point = first_x_mid_point + 1

# # The midpoit of the heiht window
# y_axis = 768
# first_y_mid_point = y_axis / 2
# second_y_mid_point = first_y_mid_point + 1

# points = [(600, 50), (600, 50), (600, 50)]
# append_list = []
# mouse_point = (500, 60)
# mouse_point_x = mouse_point[0]
# mouse_point_y = mouse_point[1]

# for index, tuple in enumerate(points):
#     element_one = tuple
#     element_x = element_one[0]
#     element_y = element_one[1]
#     if math.isclose(mouse_point_x, element_x, abs_tol = 1000) and math.isclose(mouse_point_y, element_y, abs_tol = 1000):
#         append_list.append(element_one)

# close_points = append_list[0]
# print(close_points)
# if len(close_points) < 0:
#     value = close_point[0]
#     print(close_points)
# elif len(close_points) == 0:
#     one_value = close_points
    
#     print("Hello its working it is an individual Value",close_points)
# box_x = close_points[0]
# box_y = close_points[1]
# if box_x < int(first_x_mid_point) and box_y < int(first_y_mid_point):
#     first_steps = int(first_x_mid_point) - box_x
#     second_steps = first_y_mid_point - box_y
#     pyautogui.keyDown('a')
#     sleep(5)
#     pyautogui.keyDown('w')
#     pyautogui.click(x=600, y=500)
#     if first_steps + box_x == int(first_x_mid_point) and second_steps + box_y == int(first_y_mid_point):
#         print("Am here the x axis")
#         # pyautogui.keyUp('a')
#         # pyautogui.keyDown('w')
#         print("Am here th y axis")





# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr)
 
# except KeyboardInterrupt:
#     print('\nDone')































# test = [(600, 60), (600, 70), (600, 80)]
#     x_axis = 1366
#     first_x_mid_point = x_axis / 2
#     second_x_mid_point = first_x_mid_point + 1
#     # The midpoit of the heiht window
#     y_axis = 768
#     first_y_mid_point = y_axis / 2
#     second_y_mid_point = first_y_mid_point + 1
#     append_list = []
#     mouse_point = pyautogui.position()
#     mouse_point_x = mouse_point[0]
#     mouse_point_y = mouse_point[1]
#     direction = random.randint(0,4)

#     # print(mouse_point)
#     # print(points)
#     for index, tuple in enumerate(test):
#         element_one = tuple
#         element_x = element_one[0]
#         element_y = element_one[1]
#         if math.isclose(mouse_point_x, element_x, abs_tol = 1000) and math.isclose(mouse_point_y, element_y, abs_tol = 1000):
#             append_list.append(element_one)
#     close_points = append_list[1]
#     box_x = close_points[0]
#     box_y = close_points[1]
#     # mouse_click = pyautogui.click(close_points[0], close_points[1])
#     pyautogui.moveRel(close_points[0], close_points[1])
#     if  box_x < int(first_y_mid_point):
#         pyautogui.keyUp('a')
#             # pyautogui.keyDown('i')
#         print("Am here the x axis")
#         # if box_y < int(first_y_mid_point):
#         #     second_steps = first_y_mid_point - box_y
#         #     pyautogui.keyDown('w')
#         #     pyautogui.keyDown('i')

#     #     if second_steps + box_y == int(first_y_mid_point):
#     #         pyautogui.keyUp('a')
#     #         pyautogui.keyDown('i')

#     #         print("Am here the x axis")