from math import degrees
from manim import *
from manim.opengl import *

class Test(Scene):
    def construct(self):
        surface = OpenGLSurface(
            lambda u, v: (u,v, u*np.cos(v)+v*np.cos(u)),  v_range = (-3, 3), u_range=(-3,3)
        )



        surface_mesh = OpenGLSurfaceMesh(surface)
        


        
        self.play(Create(surface_mesh))
        self.play(FadeTransform(surface_mesh, surface))

        self.interactive_embed()