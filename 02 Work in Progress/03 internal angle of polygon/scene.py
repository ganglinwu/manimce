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
            


