# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 18:36:50 2021

@author: ASUS
"""

class Rectangle():
    def __init__(self, min_x=0, min_y=0, max_x=0, max_y=0):
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y
        
def intersection_area(rect1, rect2):
    result = max(min(rect1.max_x, rect2.max_x) - max(rect1.min_x, rect2.min_x), 0) \
        * max(min(rect1.max_y, rect2.max_y) - max(rect1.min_y, rect2.min_y), 0)
    return result    
    
        
rect1 = Rectangle(0,0,3,2)
rect2 = Rectangle(1,1,3,3)

print(intersection_area(rect1, rect2))