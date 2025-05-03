from tkinter import Tk, BOTH, Canvas


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
