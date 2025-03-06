from line import Line
from window import Window
from point import Point
class Cell():
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False
        self._x1 = None

    def draw(self, x1, y1, x2, y2):
        if self._win == None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "black")
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "white")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "black")
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "white")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "black")
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "black")
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        color = None
        if undo:
            color = "gray"
        else:
            color = "red"
        from_x = (self._x2 + self._x1) // 2
        from_y = (self._y2 + self._y1) // 2
        to_x = (to_cell._x2 + to_cell._x1) // 2
        to_y = (to_cell._y2 + to_cell._y1) // 2
        print(f"from_x: {from_x}")
        print(f"from_y: {from_y}")
        print(f"to_x: {to_x}")
        print(f"to_y: {to_y}")
        line = Line(Point(from_x, from_y), Point(to_x, to_y))
        self._win.draw_line(line, color)