from manim import *


class CreateSquare(Scene):
    def construct(self):
        length = 2
        pieces = 7

        e1 = MathTex(fr"\frac{1}{pieces}").move_to([4, 2, 0])
        self.add(e1)

        square = Square(side_length=length)
        self.add(e1, square)
        self.wait(2)

        vg = VGroup()
        for i in range(pieces):
            rectangle_ = Rectangle(height=length / pieces, width=length)
            if i == 0:
                pass
            else:
                rectangle_.move_to([0, (i)*length/pieces, 0])
            vg.add(rectangle_)

        self.wait(2)
        self.play(
            ReplacementTransform(square, vg)
        )
        self.wait(5)