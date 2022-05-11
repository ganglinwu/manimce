from manim import *
import numpy as np
import math

class argandunitcircle(Scene):
    def construct(self):

        #COMPLEX PLANE
        plane = ComplexPlane().add_coordinates()
        self.add(plane)
        
        # ORIGIN
        origin = Dot(plane.n2p(0 + 0j), color = WHITE)
                

        #DOT 1
        #in order to make dot1 a variable point
        #we need to include x and y valuetrackers
        tracker = ComplexValueTracker(0+1j)
        d1 = Dot(plane.n2p(0 + 1j), color = YELLOW)
        label1 = MathTex("i").next_to(d1, UR, 0.1)


        #movable DOT 1 (update it's position)

        d1.add_updater(lambda z: z.move_to(tracker.points))

      
        
        # LINE
        line1 = Line(start = origin, end = d1, color = YELLOW)

        # movable LINE(update it's positions)
        line1.add_updater(lambda z: z.become(Line(origin.get_center(), d1.get_center())))


        self.add(origin, d1, label1, line1)

        #rotating by pi/2

        self.play(tracker.animate.set_value(tracker.get_value() * 1j))
        self.wait(2)

        #rotating by pi/2

        self.play(tracker.animate.set_value(tracker.get_value() * 1j))
        self.wait(2)

        #rotating by pi/2

        self.play(tracker.animate.set_value(tracker.get_value() * 1j))
        self.wait(2)




