from manim import *

class MatrixShrinkingAnimation(Scene):
    def construct(self):
        # Define the initial matrix
        matrix = [[0,0,0,0,0,0,0,0,0],
                  [0,0,1,1,1,1,1,1,1],
                  [0,0,2,2,3,3,3,3,3],
                  [0,0,2,5,5,7,7,8,8],
                  [0,0,2,5,6,7,11,11,13]]
        
        # Define the matrix titles
        matrix_titles = ["j/i", "0", "1", "2", "3", "4", "5", "6", "7", "8"]
        
        # Create the matrix and title objects
        matrix_mobjects = [[Text(str(matrix[i][j])) for j in range(9)] for i in range(5)]
        matrix_title_mobjects = [Text(str(matrix_titles[i])) for i in range(10)]
        
        # Position the matrix titles
        for i, title in enumerate(matrix_title_mobjects):
            title.move_to(1.5*LEFT + i*RIGHT + 2*UP)
        
        # Position the matrix
        for i, row in enumerate(matrix_mobjects):
            for j, element in enumerate(row):
                element.move_to(1.5*LEFT + j*RIGHT + (4-i)*DOWN)
        
        # Create the previous and current matrices
        prev_matrix = [0, 0, 2, 5, 5, 7, 7, 8, 8]
        curr_matrix = [0, 0, 2, 5, 6, 7, 11, 11, 13]
        
        # Create the curr array
        curr = [0, 0, 1, 2, 5, 6, 6, 7, 8]
        
        # Create the previous matrix mobjects
        prev_matrix_mobjects = [Text(str(prev_matrix[i])) for i in range(9)]
        for i, element in enumerate(prev_matrix_mobjects):
            element.move_to(1.5*LEFT + i*RIGHT + 2*DOWN)
        
        # Create the current matrix mobjects
        curr_matrix_mobjects = [Text(str(curr_matrix[i])) for i in range(9)]
        for i, element in enumerate(curr_matrix_mobjects):
            element.move_to(1.5*LEFT + i*RIGHT + 4*DOWN)
        
        # Create the curr array mobjects
        curr_mobjects = [Text(str(curr[i])) for i in range(9)]
        for i, element in enumerate(curr_mobjects):
            element.move_to(1.5*LEFT + i*RIGHT + 6*DOWN)
        
        # Add the matrix and title objects to the scene
        for row in matrix_mobjects:
            self.play(*[Write(element) for element in row])
        self.play(*[Write(title) for title in matrix_title_mobjects])
        
        # Shrink the matrix into the previous matrix
        self.wait()
        self.play(*[ApplyMethod(matrix_mobjects[i][j].move_to, prev_matrix_mobjects[j].get_center()) for i in range(1, 5) for j in range(1, 9)])
        self.wait()
        
        # Shrink the previous matrix into the current matrix
            # Shrink the current matrix into the curr array
        self.play(*[ApplyMethod(curr_matrix_mobjects[i].move_to, curr_mobjects[i].get_center()) for i in range(9)])
        self.wait()
