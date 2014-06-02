# -*- coding: utf-8 -*-
from Tkinter import Canvas, Tk
from squaretype import Rect
from rect_type import rect_types
from squaretype import Page, Rect
import pages

import math

MARGIN = 5
WIDTH = 1024
HEIGHT = 768
MIN_WIDTH = 100
MIN_HEIGHT = 60


class Rect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


class Layout():
    arrange_candidate = []

    def __init__(self, data):
        self.page_sets = pages.init(data, WIDTH, HEIGHT)

    def show_window(self):
        root = Tk()
        canvas = Canvas(root, width=WIDTH, height=HEIGHT)

        self._arrange(Rect(0, 0, WIDTH, HEIGHT))
        for page in self.pages.fixed_pages:
            canvas.create_rectangle(page.rect.x, page.rect.y, page.rect.width, page.rect.height, outline="#555", fill='#f00')
        canvas.pack()
        root.mainloop()

    def _arrange(self, rect):
        self.arrange_top_1(rect)


    def arrange_top_1(self, rect):
        top = self.pages.get_top_1()

        top_rect = None
        for type in rect_types[top[0].type]:
            height = int(math.sqrt(self.pages.ideal_area_sum(top) / type.ratio))
            width = int(type.ratio * height)
            if rect.height - height >= MIN_HEIGHT:
                top_rect = Rect(rect.x, rect.y, width, height)
                self.arrange_less_3(rect, top)
                break
        else:
            print "No fit"

        rect_under = Rect(rect.x, rect.y + top_rect.height,
                          top_rect.width, rect.height - top_rect.height)


        rect_right = Rect(rect.x + top_rect.width, rect.y,
                          rect.width - top_rect.width, rect.height)

    def arrange_less_3(self, rect, page_set):
        page_num = len(page_set)
        if page_num == 1:
            self.arrange_1(rect, page_set[0])


    def arrange_1(self, rect, page):
        page.rect = rect




























            #
    #
    #
    # def _arrange(self, rect, rest):
    #     if len(rest) == 0:
    #         return
    #
    #     if len(rest) == 1:
    #         pass
    #
    #     if len(rest) > 4:
    #         top = pages.pop_top_1()
    #         self.arrange_1(rect, rest)
    #
    #     else:
    #         self.arrange_horizontal(rect, rest)
    #         self.arrange_vertical(rect, rest)
    #
    # def _arrange_1(self, rest, rect):
    #     """
    #     1. 左上に配置する
    #     2. 右の残りスペースがMIN_WIDTH以下だったらたてにのばす
    #     3. 下の残りのスペースがMIN_HEIGHT以下だった場合に面積を小さくする
    #     4. 配置する
    #     """
    #
    #     top = self._arrange_top_pages(rest, rect)
    #
    #     rect_under = Rect(rect.x, rect.y + top.rect.height,
    #                       top.rect.width, rect.height - top.rect.height)
    #     rect_right = Rect(rect.x, rect.y + top.rect.height,
    #                       top.rect.width, rect.height - top.rect.height)
    #
    #
    #
    #
    #
    #     self._arrange()
    #
    #
    # def _set_page(self, data, rect):
    #     if not data['image'] and not data['text']:
    #         return False
    #
    #     # Extract top page
    #     # TODO: Change data structure
    #     if data['image']:
    #         top = data['image'].pop()
    #     else:
    #         top = data['text'].pop()
    #
    #     type = top.rect_type[0]
    #     height = int(math.sqrt(top.ideal_area / type.ratio))
    #     width = int(type.ratio * height)
    #     top.rect = Rect(rect.x, rect.y, width, height)
    #     return top
    #
    #
    # def arrange_horizontal(self, rect, data):
    #     width = rect.width / len(data)
    #     for i in xrange(len(data)):
    #         data[i].rect = Rect(rect.x + width * i, rect.y, width, rect.height)
    #     self.arrange(rect, 0)
    #
    #
    # def arrange_vertical(self, rect, data):
    #     pass
    #
    # def set_area(self, rect, ):
    #
    #     pass
    #

if __name__ == '__main__':
    DATA = [
        Page(4, 'image'),
        Page(8, 'image'),
        Page(6, 'image'),
        Page(10, 'image'),
        Page(2, 'image'),
        Page(9, 'text'),
        Page(7, 'text'),
        Page(5, 'text'),
        Page(3, 'text'),
        Page(1, 'text'),
        ]

    pages = Pages(DATA,  WIDTH, HEIGHT)
    layout = Layout(pages)
    layout.show_window()
    print 'hoge'
