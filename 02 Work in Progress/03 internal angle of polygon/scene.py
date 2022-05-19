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
            

#a function that draws n-sided regular polygons
#also takes in argument for centre of the polygon (x,y)
def polygon(n,x,y):
    ref_ang = 2*PI/n
    self.add(Dot((x,y), color = WHITE))
    '''
    it seems like the regular polygons with
    even number of sides have a "flat"
    top while those with odd numbers 
    have a pointy top
    so we are going to offset the first vertex
    by half the reference angle
    if the number of sides is even
    '''
    if n%2 ==0:
        first_vertex_ang = (PI/2 - 0.5*ref_ang)
    else:
        first_vertex_ang = PI/2

    '''
    loop for adding vertices
    x,y are coordinates of centre of polygon
    except for the first vertex, subsequent vertices will come with a line drawn to previous vertex
    also for the last vertex (i=n-1), we draw 2 lines
    however this seems to be time-intensive in terms of animation 
    a better way to do this might be to generate coordinates, and then append to some array,
    and animate all polygons from that array
    '''
    # for i in range(n):
    #     self.add(Dot((x+math.cos(first_vertex_ang+i*ref_ang), y+math.sin(first_vertex_ang+i*ref_ang))), color=BLUE)
    #     if i == 0:
    #         continue
    #     elif i == (n-1):
    #         self.add(Line(start=(x+math.cos(first_vertex_ang+n*ref_ang), y+math.sin(first_vertex_ang+n*ref_ang)), end =(x+math.cos(first_vertex_ang), y+math.sin(first_vertex_ang)), color=WHITE))
    #     else:
    #         self.add(Line(start=(x+math.cos(first_vertex_ang+i*ref_ang), y+math.sin(first_vertex_ang+i*ref_ang)), end=(x+math.cos(first_vertex_ang+(i-1)*ref_ang), y+math.sin(first_vertex_ang+(i-1)*ref_ang)), color=WHITE))

    '''
    hopefully this makes for better animations as mentioned above
    '''
    coord=[(x+math.cos(first_vertex_ang),y+math.sin(first_vertex_ang))]
    for i in range(n):
        coord.append((x+math.cos(first_vertex_ang+i*ref_ang),y+math.sin(first_vertex_ang+i*ref_ang)))
    return coord
