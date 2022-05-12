from manim import *


class argandunitcircle(MovingCameraScene):
    def construct(self):

        #save camera state
        self.camera.frame.save_state()

        #COMPLEX PLANE
        plane = ComplexPlane().add_coordinates()
        self.play(Create(plane, run_time = 2, lag_ratio=0.1))
        self.wait()
        
        # ORIGIN
        origin = Dot(plane.n2p(0 + 0j), color = WHITE)
                

        #DOT 1
        #in order to make dot1 a variable point
        #we need to include x and y valuetrackers
        tracker = ComplexValueTracker(0+1j)
        d1 = Dot(plane.n2p(0 + 1j), color = YELLOW)




        #movable DOT 1 (update it's position)

        # d1.add_updater(lambda z: z.move_to(tracker.points))
        
      
        
        # LINE
        line1 = Line(start = origin, end = d1, color = YELLOW)

        # movable LINE(update it's positions)
        line1.add_updater(lambda z: z.become(Line(origin.get_center(), d1.get_center(), color = YELLOW)))


        #animating origin, DOT 1 and LINE 1
        self.play(
                Create(origin), 
                Create(d1)
        )
        self.play(Create(line1))
        self.wait()

        #changing camera
        self.play(self.camera.frame.animate.scale(0.5))

        #label(title) for i^n
        title1 = MathTex(r"i^1").shift(UP + LEFT)
        self.play(Write(title1))


        #animation before first rotation
        self.play(Wiggle(line1))
        self.wait()

        #rotating by FIRST pi/2

        self.play(Unwrite(title1))
        title2 = MathTex(r"i^2").shift(UP + LEFT)
        self.play(Write(title2))
        tracker.set_value(-1 + 0j)
        self.play(
            Rotating(
                d1,
                radians = PI/2,
                about_point=ORIGIN,
                run_time = 1
            )
        )
        self.update_mobjects(0)
        self.wait()
        self.play(Wiggle(line1))
        self.wait(2)

        #rotating by SECOND pi/2

        self.play(Unwrite(title2))
        title3 = MathTex(r"i^3").shift(UP + LEFT)
        self.play(Write(title3))
        tracker.set_value(0 - 1j)
        self.play(
            Rotating(
                d1,
                radians = PI/2,
                about_point=ORIGIN,
                run_time = 1
            )
        )
        self.update_mobjects(0)
        self.wait()
        self.play(Wiggle(line1))
        self.wait(2)

        #rotating by THIRD pi/2

        self.play(Unwrite(title3))
        title4 = MathTex(r"i^4").shift(UP + LEFT)
        self.play(Write(title4))
        tracker.set_value(1 + 0j)
        self.play(
            Rotating(
                d1,
                radians = PI/2,
                about_point=ORIGIN,
                run_time = 1
            )
        )
        self.update_mobjects(0)
        self.wait(2)