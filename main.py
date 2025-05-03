from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width=400, height=400):

        self.__root = Tk()
        self.__root.geometry(f"{width}x{height}")
        self.__root.title("Maze Solver")

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


def main():
    win = Window(800, 600)
    win.wait_for_close()


if __name__ == "__main__":
    main()
