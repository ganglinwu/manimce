#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 11:07:14 2021

@author: ganglinwu
"""

from manim import *
import numpy as np
import math

class GPsumofrecurring9(MovingCameraScene):
    def construct(self):
        
        t1 = MathTex(r"0.\dot{9} = 0.999999...")
        

        self.play(FadeIn(t1))

        
        self.play(t1.animate.shift([0,3,0]), run_time=2)
        self.wait()
        
        self.camera.frame.save_state()
        
        self.play(self.camera.frame.animate.scale(0.6).move_to(UP), run_time=2)
        
        
        arr_group = VGroup(*list(Arrow(start=[-0.258+0.258*i, 2.9, 0], end=[-0.258+0.258*i, 2.4-0.60*i, 0], stroke_width=1, stroke_opacity=0.2) for i in range (0,7)))
        self.play(FadeIn(arr_group), run_time=1)
            
        dot_group = VGroup(*list(Dot(point=[-0.258+0.258*j, 2.4-0.60*j, 0]) for j in range(0,6)))    
        decimal_group = VGroup(*list(MathTex("0." + j*"0" + "9", font_size=21, color=BLUE).next_to(dot_group[j], direction=DOWN+0.3*RIGHT) for j in range(0,6)))
        
#here we see three VGroups with list comprehension. What I wanted to do was to create e.g.
# arrow1 = mobject1
# arrow2 = mobject 2
# etc.. 
# the first challenge was to group up all these arrows because I want all of them to disappear,
# or for all the decimals to transform into a straight line
# thus we need to have different variable names for all these mobjects
# since we cannot create different variable names in a for loop
# the solution was to do list comprehension in the VGroup
        
        
        self.play(FadeIn(decimal_group), run_time=2)
        self.wait()
        
        
        
        test_group = VGroup(arr_group, decimal_group)
        t2 = MathTex("= 0.9 + 0.09 + 0.009 + 0.0009 + 0.00009 + 0.000009 + ...", font_size=45, color=BLUE)
        self.play(Transform(test_group, t2), run_time=2)
        
        self.play(Restore(self.camera.frame), run_time=1)
        
        self.play(t1.animate.shift([-4.1,0,0]), run_time=1)
        self.play(t2.animate.shift([0.4, 2, 0]), run_time = 2)
        self.play(FadeOut(test_group), run_time = 2)
        
        t3 = MathTex(r"= \frac{9}{10^1} + \frac{9}{10^2} + \frac{9}{10^3} + \frac{9}{10^4} + \frac{9}{10^5} + \frac{9}{10^6} +...", font_size=45, color=BLUE)
        t3.shift([-0.6,2,0])
        self.play(Transform(t2, t3), run_time = 3)
        
        self.wait(2)
        
        
        t4 = MathTex(r"= \sum_{n=1}^{\infty} \frac{9}{10^n}", font_size=45, color=BLUE)
        t4.shift([-4.1, 0.5, 0])
        self.play(FadeIn(t4), run_time = 2)
    
        
        t5 = MathTex(r"= \frac{a}{1-r}", font_size=45, color = BLUE)
        t5.shift([-4.3, -1 , 0])
        t6 = MathTex(r"= \frac{0.9}{1-0.1}", font_size=45, color = BLUE)
        t6.shift([-4.1, -1 , 0])
        t7 = MathTex(r"= \frac{0.9}{0.9}", font_size=45, color = BLUE)
        t7.shift([-4.5, -1 , 0])

        
        self.play(FadeIn(t5), run_time = 2)
        self.wait(2)
        self.play(Transform(t5, t6), run_time = 2)
        self.wait(2)
        self.play(Transform(t5, t7), run_time = 2)
        self.wait(2)
        
        t8 = MathTex("= 1", font_size=45, color = BLUE)
        t8.shift([-4.8, -2 , 0])
        self.play(FadeIn(t8), run_time = 2)
        
        t9 = MathTex(r"0.\dot{9}", font_size=45)
        t9.shift([-5.6, -1.95 , 0])
        self.play(FadeIn(t9), run_time = 3)
        
    
            


