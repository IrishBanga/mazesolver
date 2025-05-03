from tkinter import Tk, BOTH, Canvas
import time, random


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def draw(self, canvas: Canvas, fill_color="black"):
        canvas.create_line(
            self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=2
        )


class Cell:
    def __init__(
        self, l_top: Point, r_bottom: Point, l_wall, r_wall, t_wall, b_wall, window
    ):
        self.l_top = l_top
        self.r_bottom = r_bottom
        self.l_wall = l_wall
        self.r_wall = r_wall
        self.t_wall = t_wall
        self.b_wall = b_wall
        self.visited = False
        self.lines = []
        self.window = window

    def draw(self, l_top: Point, r_bottom: Point):
        if self.l_wall:
            self.lines.append(Line(l_top, Point(l_top.x, r_bottom.y)))
        if self.r_wall:
            self.lines.append(Line(Point(r_bottom.x, l_top.y), r_bottom))
        if self.t_wall:
            self.lines.append(Line(l_top, Point(r_bottom.x, l_top.y)))
        if self.b_wall:
            self.lines.append(Line(Point(l_top.x, r_bottom.y), r_bottom))

        for line in self.lines:
            self.window.draw_line(line, "black")

    def draw_move(self, dest_cell, undo=False):
        fill_color = "red" if undo else "gray"
        start = Point(
            (self.l_top.x + self.r_bottom.x) / 2, (self.l_top.y + self.r_bottom.y) / 2
        )
        end = Point(
            (dest_cell.l_top.x + dest_cell.r_bottom.x) / 2,
            (dest_cell.l_top.y + dest_cell.r_bottom.y) / 2,
        )

        line = Line(start, end)
        self.window.draw_line(line, fill_color)


class Maze:
    def __init__(self, x, y, rows, cols, cell_width, cell_height, window=None):
        self.x = x
        self.y = y
        self.rows = rows
        self.cols = cols
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.window = window

        self.cells = []
        self._create_cells()

    def _create_cells(self):
        for i in range(self.cols):
            column = []
            for j in range(self.rows):
                l_top = Point(
                    self.x + i * self.cell_width, self.y + j * self.cell_height
                )
                r_bottom = Point(l_top.x + self.cell_width, l_top.y + self.cell_height)
                if i == 0 and j == 0:
                    cell = Cell(l_top, r_bottom, True, True, False, True, self.window)
                elif i == self.cols - 1 and j == self.rows - 1:
                    cell = Cell(l_top, r_bottom, True, True, True, False, self.window)
                else:
                    cell = Cell(l_top, r_bottom, True, True, True, True, self.window)

                column.append(cell)
            self.cells.append(column)

    def _draw_cells(self):
        for column in self.cells:
            for cell in column:
                cell.draw(cell.l_top, cell.r_bottom)
                self._animate()

    def _animate(self):
        self.window.redraw()
        time.sleep(0.05)

    def _break_walls(self, x, y):
        self.cells[x][y].visited = True
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while True:
            next_moves = [
                (x + d[0], y + d[1])
                for d in directions
                if 0 <= x + d[0] < self.cols and 0 <= y + d[1] < self.rows
                if not self.cells[x + d[0]][y + d[1]].visited
            ]

            if not next_moves:
                return

            next_x, next_y = random.choice(next_moves)

            diff_x = next_x - x
            diff_y = next_y - y
            if diff_x == 1:
                self.cells[x][y].r_wall = False
                self.cells[next_x][next_y].l_wall = False
            elif diff_x == -1:
                self.cells[x][y].l_wall = False
                self.cells[next_x][next_y].r_wall = False
            elif diff_y == 1:
                self.cells[x][y].b_wall = False
                self.cells[next_x][next_y].t_wall = False
            elif diff_y == -1:
                self.cells[x][y].t_wall = False
                self.cells[next_x][next_y].b_wall = False

            self._break_walls(next_x, next_y)


class Window:
    def __init__(self, width=400, height=400):

        self.__root = Tk()
        self.__root.geometry(f"{width}x{height}")
        self.__root.title("Maze Solver")
        self.__root.resizable(False, False)

        self.canvas = Canvas(self.__root, bg="white")
        self.canvas.pack(fill=BOTH, expand=True)

        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line: Line, fill_colour):
        line.draw(self.canvas, fill_colour)


def main():
    win = Window(800, 600)
    win.wait_for_close()


if __name__ == "__main__":
    main()
