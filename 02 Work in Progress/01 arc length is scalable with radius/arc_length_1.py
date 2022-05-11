#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 15:04:57 2021

@author: ganglinwu
"""

from manim import *
import numpy as np
import math

class arclengthscaling(Scene):
    def construct(self):
        circle = Circle(1,stroke_color=BLUE, stroke_opacity=0.5).shift(LEFT)
        arc = Arc(1, start_angle=0, angle=1, stroke_color=RED,stroke_opacity=1).shift(LEFT)
        
        rotation_centre = LEFT
        theta_tracker = ValueTracker(0.01) #valuetracker = 0 will cause lines do not intersect error
        
        line1 = Line(LEFT,ORIGIN)
        line_moving = Line(LEFT, ORIGIN, stroke_color=RED)
        line_ref = line_moving.copy()
        line_moving.rotate(
            theta_tracker.get_value() * DEGREES, about_point = rotation_centre
            )
        a = Angle(line1, line_moving, radius=0.5, other_angle=False)
        tex = MathTex(r"\theta").move_to(
            Angle(
                line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
            ).point_from_proportion(0.5)
        )
        
        
        self.play(Create(circle)) #draws a circle on the screen Quadrant 1 to Q4
        self.wait()
        self.add(line1,line_moving)
        self.wait()


        line_moving.add_updater(
            lambda x: x.become(line_ref.copy()).rotate(
                theta_tracker.get_value() * DEGREES, about_point=rotation_centre
            )
        )

        a.add_updater(
            lambda x: x.become(Angle(line1, line_moving, radius=0.5, other_angle=False))
        )
        tex.add_updater(
            lambda x: x.move_to(
                Angle(
                    line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
                ).point_from_proportion(0.5)
            )
        )

        

        
    
        self.play(theta_tracker.animate.set_value(57.325))
        self.play(Create(arc))
        
        
        