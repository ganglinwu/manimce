#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 12:41:36 2021

@author: ganglinwu
"""

from manim import *
import numpy as np
import math

class diffareaoftriangles(MovingCameraScene):
    def construct(self):
       
        A = Dot(color=WHITE, point=[0,1,0])
        B = Dot(color=WHITE, point=[0,0,0])
        C = Dot(color=WHITE, point=[1,0,0])
        lineAB = Line(A.get_center(), B.get_center(), color=BLUE)
        lineBC = Line(B.get_center(), C.get_center(), color=BLUE)
        lineCA = Line(C.get_center(), A.get_center(), color=BLUE)
        
        group = VGroup(A, B, C, lineAB, lineBC, lineCA)
        
        
        self.play(Create(A))
        self.play(Create(B))
        self.play(Create(C))
        self.wait(0.5)
        
        self.play(Create(lineAB))        
        self.play(Create(lineBC))
        self.play(Create(lineCA))
        self.wait()
        
        self.play(group.animate.shift([-6,2,0]))
        self.wait()

        b1 = BraceBetweenPoints([-6,3,0],[-6,2,0])
        b2 = BraceBetweenPoints([-6,2,0],[-5,2,0])
        b1tex = b1.get_tex("1")
        b2tex = b2.get_tex("1")

        self.play(Create(b1))
        self.play(Create(b1tex))
        self.play(Create(b2))
        self.play(Create(b2tex))

        
        D = Dot(color=WHITE, point=[0,1,0])
        E = Dot(color=WHITE, point=[0,0,0])
        F = Dot(color=WHITE, point=[1,0,0])
        lineDE = Line(D.get_center(), E.get_center()).set_color(YELLOW)
        lineEF = Line(E.get_center(), F.get_center(), color=BLUE)
        lineFD = Line(F.get_center(), D.get_center(), color=BLUE)
        arc = Arc(radius=1, start_angle=PI/2, angle=PI/2, stroke_opacity=0)
        arc2 = Arc(radius=1, start_angle=PI, angle=-PI/2, stroke_opacity=0)
        circle = Circle(radius=1, color=WHITE, stroke_opacity=0)
        
        group1 = VGroup(D, E, F, lineDE, lineEF, lineFD, circle, arc, arc2)
        
        self.play(Create(D))
        self.play(Create(E))
        self.play(Create(F))
        self.wait(0.5)
        self.play(Create(lineDE))
        self.play(Create(lineEF))
        self.play(Create(lineFD))
        self.wait()
        self.play(group1.animate.shift([4,2,0]))
        self.wait()
        
        lineDE.add_updater(lambda z: z.become(Line(D.get_center(), E.get_center()))).set_color(YELLOW)
        lineFD.add_updater(lambda z: z.become(Line(F.get_center(), D.get_center()))).set_color(BLUE)
        # so these two lines with the add_updater asks manim to keep recreating the lines as the point D moves
        
        
        self.play(MoveAlongPath(D, arc), run_time=2, rate_func=linear)
        #point D is going to move along the "circle" from pi/2 to pi(we have defined an arc just for this movement)
                    
        for i in range(1,5):
            if i == 1: # i just wanted to remove the "moving" triangle while the 4 smaller triangles were being created..
                self.remove(lineDE.add_updater)
                self.remove(lineFD.add_updater)
                self.play(FadeOut(group1))
            i = i*math.pi/8
            a,b,c = Dot([(-6 + 5*i + math.cos((4+i)/8*math.pi)),(math.sin((4-i)*math.pi/8)+2),0]), Dot([(-6 + 5*i),2,0]), Dot([(-5 + 5*i),2,0])
            line1, line2, line3 = Line(a.get_center(), b.get_center()).set_color(BLUE), Line(b.get_center(), c.get_center()).set_color(BLUE), Line(c.get_center(), a.get_center()).set_color(BLUE)
            br = Brace(line2)
            brtext = br.get_text("1")
            group = VGroup(a,b,c,line1, line2, line3, br, brtext)
            self.play(FadeIn(group))
        
        self.wait()
        
        new_center = Dot([-2,1,0], color=GREY, stroke_opacity=0.01)
        # this will be the new centre frame of reference for the moving camera
        
        self.play(self.camera.frame.animate.move_to(new_center))
        
        
        text = Text("Which of these triangles has the greatest area?", font_size=35).shift(1.5*LEFT)
        self.play(Create(text))
        
        self.camera.frame.save_state()
        #we are going to "zoom in" later on.. in order to return to this exact frame, let's save it
        
        line4 = DashedLine(start=[-6,3,0], end =[3,3,0], color = ORANGE, stroke_width=0.2)
        self.play(Create(line4))   
        
        self.play(self.camera.frame.animate.scale(0.1).move_to(A), run_time=5)
        for k in range(4):
            self.play(self.camera.frame.animate.move_to([(-4+2*k+math.cos((4+k)/8*math.pi)),3,0]), run_time=3)
        self.play(Restore(self.camera.frame), run_time = 3)
        
        self.wait()

       