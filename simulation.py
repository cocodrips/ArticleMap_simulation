# -*- coding: utf-8 -*-
from Tkinter import Canvas, Tk
from squaretype import Rect
from rect_type import rect_types
from squaretype import Page, Rect
import types
import pages
import copy

import math

MARGIN = 5
WIDTH = 1024
HEIGHT = 768
MIN_WIDTH = 100
MIN_HEIGHT = 60


class Layout():
    arrange_candidate = []

    def __init__(self, data, width, height):
        self.page_sets = pages.init(data, width, height)

    def show_window(self):
        root = Tk()
        canvas = Canvas(root, width=WIDTH, height=HEIGHT)

        self._arrange(self.page_sets, Rect(0, 0, WIDTH, HEIGHT), False)

        for page_set in self.page_sets:
            page = page_set[0]
            if page.rect:
                canvas.create_rectangle(page.rect.x, page.rect.y, page.rect.width, page.rect.height,
                                        outline="#555", fill='#f00')
        canvas.pack()
        root.mainloop()

    def _arrange(self, page_sets, rect, is_grouped=True):
        """
        Args:
            page_sets: [[], [], []]
            is_grouped (Boolean)
        """

        if not page_sets:
            return

        # [[], [], []]
        if type(page_sets[0]) == types.ListType:
            if len(page_sets) > 3:
                self.arrange_top_1(page_sets, rect, is_grouped)
            else:
                self.arrange_less_3(page_sets, rect)

        # [ , , ]
        else:
            self.arrange_less_3(page_sets, rect)


    def arrange_top_1(self, page_sets, rect, is_grouped):
        top = pages.get_top_1(page_sets)

        top_rect = None
        for type in rect_types[top[0].type]:
            height = int(math.sqrt(pages.ideal_area_sum(top) / type.ratio))
            width = int(type.ratio * height)
            if rect.height - height >= MIN_HEIGHT:
                top_rect = Rect(rect.x, rect.y, width, height)
                self._arrange(top, top_rect)
                break
        else:
            raise Warning

        page_sets = self.new_sets(page_sets, top)

        if not is_grouped:
            page_sets = pages.grouping_page_sets(page_sets)
        rect_under = Rect(rect.x, rect.y + top_rect.height,
                          top_rect.width, rect.height - top_rect.height)

        page_sets = self.get_optimum_sets(page_sets, rect_under)

        rect_right = Rect(rect.x + top_rect.width, rect.y,
                          rect.width - top_rect.width, rect.height)

        self._arrange(page_sets, rect_right)

    def arrange_less_3(self, page_sets, rect, ):
        """
        Args:
            page_sets: [[],[],[]] or [ , , ]
        """
        self.arrange_vertical(page_sets, rect)

        # length = len(page_sets)
        #
        # horizontal = (rect.width / length) / float(rect.height)
        # vertical = rect.width / float(rect.height / length)
        #
        # aspect = None
        # [[], [], []]
        # if type(page_sets[0]) == types.ListType:
        #     aspect = rect_types[page_sets[0][0].type]
        #     self.arrange_vertical(page_sets, rect)
        #
        #     # [ , , ]
        # else:
        #     aspect = rect_types[page_sets[0][0].type]
        #     self.arrange_vertical(page_sets, rect)

    def get_optimum_sets(self, page_sets, rect):
        selected = pages.get_optimum_set(page_sets, rect)
        self._arrange(selected, rect)
        return self.new_sets(page_sets, selected)


    def arrange_vertical(self, page_sets, rect):
        length = len(page_sets)
        width = rect.width / length

        if type(page_sets[0]) == types.ListType:
            for i in xrange(length):
                pages_rect = Rect(rect.x + width * i, rect.y, width, rect.height)
                self._arrange(page_sets[i], pages_rect)

        else:
            for i in xrange(length):
                page_sets[i].rect = Rect(rect.x + width * i, rect.y, width, rect.height)
                # fin


    def arrange_horizontal(self, page_sets, rect):
        pass

    #TODO: Naming
    def set_optimum(self, page_sets, rect):
        optimum_set = pages.get_optimum_set(page_sets, rect)
        self._arrange(optimum_set, rect)


    def arrange_1(self, rect, page):
        page.rect = rect


    def new_sets(self, page_sets, page_set):
        new_sets = []
        for page_set in page_sets:
            if page_set != page_set:
                new_sets.append(page_set)
        return new_sets


























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

    layout = Layout(DATA, WIDTH, HEIGHT)
    layout.show_window()
    print 'hoge'
