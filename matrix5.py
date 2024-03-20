from manim import *

class KnapsackMatrix(Scene):
    def construct(self):
        # Define the matrix dimensions and values
        n = 4
        m = 8
        profit = [1, 2, 5, 6]
        weight = [2, 3, 4, 5]

        # Create the matrix and initialize it with zeros
        matrix = [[0 for j in range(m+1)] for i in range(n+1)]

        # Fill in the matrix with the correct values
        for i in range(1, n+1):
            for j in range(1, m+1):
                if weight[i-1] <= j:
                    matrix[i][j] = max(matrix[i-1][j], matrix[i-1][j-weight[i-1]] + profit[i-1])
                else:
                    matrix[i][j] = matrix[i-1][j]

        # Define the position of the matrix
        matrix_pos = [-3, 2, 0]

        # Create the text labels for the rows and columns
        rows = [Tex(str(i)).set_color(WHITE) for i in range(n+1)]
        columns = [Tex(str(i)).set_color(WHITE) for i in range(m+1)]

        # Set the position of the row and column labels
        for i, row in enumerate(rows):
            row.move_to([matrix_pos[0]-0.75, matrix_pos[1]-i*0.75, 0])
        for i, col in enumerate(columns):
            col.move_to([matrix_pos[0]+i*0.75, matrix_pos[1]+0.75, 0])

        # Create the cells of the matrix
        cells = []
        for i, row in enumerate(matrix):
            cell_row = []
            for j, cell in enumerate(row):
                cell_label = Tex(str(cell)).set_color(WHITE)
                cell_label.move_to([matrix_pos[0]+j*0.75, matrix_pos[1]-i*0.75, 0])
                cell_rect = Rectangle(width=0.7, height=0.7, fill_opacity=0, stroke_opacity=1, stroke_width=0.05, color=WHITE)
                cell_rect.move_to([matrix_pos[0]+j*0.75, matrix_pos[1]-i*0.75, 0])
                cell_row.append([cell_label, cell_rect])
            cells.append(cell_row)

        # Add the row and column labels and cells to the scene
        for row in rows:
            self.add(row)
        for col in columns:
            self.add(col)
        for cell_row in cells:
            for cell in cell_row:
                self.add(cell[1])
                self.add(cell[0])

        # Animate the filling of the cells in the matrix
        for i, row in enumerate(cells):
            for j, cell in enumerate(row):
                self.play(Write(cell[0]), run_time=0.5)
