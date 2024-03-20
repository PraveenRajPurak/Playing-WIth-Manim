from manim import *

class MatrixAnimation(Scene):
    def construct(self):
        # Create initial matrix
        matrix = [[1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1]]

        # Create matrix object
        matrix_mobj = Matrix(matrix).set_hfill(0.7).set_vfill(0.7)
        self.play(Create(matrix_mobj))

        # Create s2 matrix
        s2_matrix = [[1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]]
        s2_matrix_mobj = Matrix(s2_matrix).set_hfill(0.7).set_vfill(0.7)

        # Create shrinking animation for matrix to s2_matrix
        self.play(Transform(matrix_mobj, s2_matrix_mobj), run_time=2)

        # Create curr matrix
        curr = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
        curr_matrix_mobj = Matrix([curr]).set_hfill(0.7).set_vfill(0.7)

        # Create shrinking animation for s2_matrix to curr_matrix
        self.play(Transform(matrix_mobj, curr_matrix_mobj), run_time=2)

        self.wait(1)
