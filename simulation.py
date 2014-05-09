# -*- coding: utf-8 -*-
from Tkinter import Canvas, Tk
from squaretype import LayoutTypes, Rect
import math

MARGIN = 5
WIDTH = 1024
HEIGHT = 768
MIN_LENGTH = 100


class Rect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


class Layout():
    data = []
    arrange_candidate = []

    def __init__(self, pages):
        self.pages = pages

    def show_window(self):
        root = Tk()
        canvas = Canvas(root, width=WIDTH, height=HEIGHT)
        canvas.pack()
        root.mainloop()
        self._arrange(self.data, Rect(0, 0, WIDTH, HEIGHT))

    def _arrange(self, rect, rest):
        if len(rest) == 0:
            return

        if len(rest) == 1:
            pass

        if len(rest) > 4:
            self.arrange_1(rect, rest)

        else:
            self.arrange_horizontal(rect, rest)
            self.arrange_vertical(rect, rest)

    def _arrange_1(self, data, rect):
        top = self._arrange_top_pages(data, rect)

        rect_under = Rect(rect.x, rect.y + top.rect.height,
                          top.rect.width, rect.height - top.rect.height)

        rect_right = Rect(rect.x, rect.y + top.rect.height,
                          top.rect.width, rect.height - top.rect.height)

    def _set_page(self, data, rect):
        if not data['image'] and not data['text']:
            return False

        # Extract top page
        # TODO: Change data structure
        if data['image']:
            top = data['image'].pop()
        else:
            top = data['text'].pop()

        type = top.rect_type[0]
        height = int(math.sqrt(top.ideal_area / type.ratio))
        width = int(type.ratio * height)
        top.rect = Rect(rect.x, rect.y, width, height)
        return top


    def arrange_horizontal(self, rect, data):
        width = rect.width / len(data)
        for i in xrange(len(data)):
            data[i].rect = Rect(rect.x + width * i, rect.y, width, rect.height)
        self.arrange(rect, 0)


    def arrange_vertical(self, rect, data):
        pass

    def set_area(self, rect, ):

        pass





