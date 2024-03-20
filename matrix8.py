from manim import *

class MatrixAnimation(Scene):
    def construct(self):
        # Create initial matrix
        matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 1, 1, 1, 1, 1, 1],
                  [0, 0, 2, 2, 3, 3, 3, 3, 3],
                  [0, 0, 2, 5, 5, 7, 7, 8, 8]]
        
        # Create matrix object
        matrix_mobj = Matrix(matrix).set_hfill(0.7).set_vfill(0.7)
        self.play(Create(matrix_mobj))

        # Create shrinking animation
        prev_matrix = [0, 0, 2, 5, 5, 7, 7, 8, 8]
        curr_matrix = [0, 0, 2, 5, 6, 7, 11, 11, 13]

        # Create previous matrix object
        prev_matrix_mobj = Matrix([prev_matrix]).next_to(matrix_mobj, DOWN, buff=1)
        self.play(Transform(matrix_mobj, prev_matrix_mobj))

        # Create current matrix object
        curr_matrix_mobj = Matrix([curr_matrix]).next_to(matrix_mobj, DOWN, buff=1)
        self.play(Transform(matrix_mobj, curr_matrix_mobj))

        self.wait(1)
