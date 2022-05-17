import math
from manim import *

class polygonintangle(MovingCameraScene):
    def construct(self):

        #save camera state
        self.camera.frame.save_state()

        #draw polygons
        #we want to use a loop to draw multiple
        #REGULAR polygons

        n = 10 #number of sides of largest polygon
        for i in range (4,n+1):
            

#a function that draws polygons
def polygon(n):
    ref_ang = 2*PI/n
    #it seems like the regular polygons with
    #even number of sides have a "flat"
    #top while those with odd numbers 
    #have a pointy top
    #so we are going to offset the first vertex
    #by half the reference angle
    #if the number of sides is even
    if n%2 ==0:
        first_vertex_ang = (PI/2 - 0.5*ref_ang)
    else:
        first_vertex_ang = PI/2

