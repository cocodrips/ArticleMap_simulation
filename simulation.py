# -*- coding: utf-8 -*-
from Tkinter import Canvas, Tk
from squaretype import Rect
from rect_type import rect_types
from squaretype import Page, Rect
import types
import pages
from itertools import chain

import copy

import math

MARGIN = 5
WIDTH = 1024
HEIGHT = 768
MIN_WIDTH = 100
MIN_HEIGHT = 60
ERROR = 10


class Layout():
    arrange_candidate = []

    def __init__(self, data, width, height):
        self.page_sets = pages.init(data, width, height)

    def show_window(self):
        root = Tk()
        canvas = Canvas(root, width=WIDTH, height=HEIGHT)

        self._arrange(self.page_sets, Rect(2, 2, WIDTH, HEIGHT), False)
        # self._adjust_line(self.page_sets)


        for page_set in self.page_sets:
            page = page_set[0]
            if page.rect:
                canvas.create_rectangle(page.rect.x, page.rect.y, page.rect.x + page.rect.width,
                                        page.rect.y + page.rect.height,
                                        outline="#555")
                canvas.create_text(page.rect.x + page.rect.width / 2, page.rect.y + 10,
                                   text=str(page.priority))
                print page.priority, page.rect
        canvas.pack()
        root.mainloop()

    def _adjust_line(self, page_sets):
        l = list(chain.from_iterable(page_sets))
        for i in xrange(len(l)):
            for j in xrange(i+1, len(l)):
                if abs(l[i].rect.x - l[j].rect.x) < 10:
                    l[i].rect.x = l[j].rect.x = max(l[i].rect.x, l[j].rect.x)
                if abs(l[i].rect.y - l[j].rect.y) < 10:
                    l[i].rect.y = l[j].rect.y = max(l[i].rect.y, l[j].rect.y)



    def _arrange(self, page_sets, rect, is_grouped=True):
        """
        Args:
            page_sets: [[], [], []]
            is_grouped (Boolean)d
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
            # TODO: ?
            page_sets.sort(key=lambda x: x.priority, reverse=True)
            self.arrange_pages(page_sets, rect)



    def arrange_top_1(self, page_sets, rect, is_grouped):
        top = pages.get_top_1(page_sets)

        top_rect = None
        for type in rect_types[top[0].type]:

            # yoko
            height = int(math.sqrt(pages.ideal_area_sum(top) / type.ratio))
            width = int(type.ratio * height)
            if rect.height - height >= MIN_HEIGHT:
                top_rect = Rect(rect.x, rect.y, width, height)
                self._arrange(top, top_rect)
                break

            # tate
            height = int(math.sqrt(pages.ideal_area_sum(top) / (type.ratio / len(top))))
            width = int(pages.ideal_area_sum(top) / height)
            if rect.height - height >= MIN_HEIGHT:
                top_rect = Rect(rect.x, rect.y, width, height)
                self._arrange(top, top_rect)
                break


        else:
            raise Warning

        page_sets = self.new_sets(page_sets, top)

        if not is_grouped:
            page_sets = pages.grouping_page_sets(page_sets)
            page_sets.sort(cmp=pages.page_cmp, reverse=True)
        rect_under = Rect(rect.x, rect.y + top_rect.height,
                          top_rect.width, rect.height - top_rect.height)

        page_sets = self.get_optimum_sets(page_sets, rect_under)

        rect_right = Rect(rect.x + top_rect.width, rect.y,
                          rect.width - top_rect.width, rect.height)

        self._arrange(page_sets, rect_right)

    def arrange_less_3(self, page_sets, rect):
        """
        Args:
            page_sets: [[],[],[]] or [ , , ]
        """
        if rect.height < rect.width:
            self.arrange_vertical(page_sets, rect)
        else:
            self.arrange_horizontal(page_sets, rect)

    def get_optimum_sets(self, page_sets, rect):
        selected = pages.get_optimum_set(page_sets, rect)
        self._arrange(selected, rect)
        return self.new_sets(page_sets, selected)


    def arrange_vertical(self, page_sets, rect):
        sets_priority_sum = pages.priority_sum(page_sets)
        last_x = rect.x
        for page_set in page_sets:
            priority_ratio = 1.0 * pages.priority_sum(page_set) / sets_priority_sum
            width = rect.width * priority_ratio
            new_rect = Rect(last_x, rect.y, width, rect.height)
            last_x += width

            if self.is_group(page_set):
                self._arrange(page_set, new_rect)
            else:
                page_set.rect = new_rect

    def arrange_horizontal(self, page_sets, rect):
        sets_priority_sum = pages.priority_sum(page_sets)
        last_y = rect.y
        for page_set in page_sets:
            priority_ratio = 1.0 * pages.priority_sum(page_set) / sets_priority_sum
            height = rect.height * priority_ratio
            new_rect = Rect(rect.x, last_y, rect.width, height)
            last_y += height

            if self.is_group(page_set):
                self._arrange(page_set, new_rect)
            else:
                page_set.rect = new_rect

    def arrange_pages(self, page_set, rect):
        length = len(page_set)
        # TODO: Write devide algorithm

        ideal_ratio = rect_types[page_set[0].type][0].ratio
        rect_ratio = float(rect.width) / rect.height

        print 'yoko',(rect_ratio / len(page_set) - ideal_ratio)
        print 'tate',  (rect_ratio * len(page_set) - ideal_ratio)
        if (abs(1 - (rect_ratio / len(page_set) - ideal_ratio))
            > abs(1 - (rect_ratio * len(page_set) - ideal_ratio))):
            print page_set
            self.arrange_pages_vertical(page_set, rect)
        else:
            self.arrange_pages_horizontal(page_set, rect)


    def arrange_pages_vertical(self, page_set, rect):
        height = rect.height / len(page_set)

        for i, page in enumerate(page_set):
            page.rect = Rect(rect.x, rect.y + height * i, rect.width, height)

    def arrange_pages_horizontal(self, page_set, rect):
        width = rect.width / len(page_set)

        for i, page in enumerate(page_set):
            page.rect = Rect(rect.x + width * i, rect.y, width, rect.height)


    #TODO: Naming
    def set_optimum(self, page_sets, rect):
        optimum_set = pages.get_optimum_set(page_sets, rect)
        self._arrange(optimum_set, rect)


    def arrange_1(self, rect, page):
        page.rect = rect

    def new_sets(self, page_sets, target_page):
        new_sets = []
        for page_set in page_sets:
            if page_set != target_page:
                new_sets.append(page_set)
        return new_sets

    def is_group(self, page_sets):
        return type(page_sets) == types.ListType


if __name__ == '__main__':
    DATA = [
        Page(4, 'image'),
        Page(8, 'image'),
        Page(6, 'image'),
        Page(10, 'image'),
        Page(12, 'image'),
        Page(2, 'image'),
        Page(11, 'text'),
        Page(9, 'text'),
        Page(7, 'text'),
        Page(5, 'text'),
        Page(3, 'text'),
        Page(1, 'text'),
    ]

    # DATA = [
    #     Page(4, 'image'),
    #     Page(8, 'image'),
    #     Page(6, 'image'),
    #     Page(11, 'image'),
    #     Page(5, 'image'),
    #     Page(9, 'text'),
    #     Page(1, 'text'),
    #     Page(5, 'text'),
    #     Page(30, 'text'),
    #     Page(10, 'text'),
    #     Page(9, 'text'),
    #     Page(1, 'text'),
    #     Page(5, 'text'),
    #     Page(30, 'text'),
    #     Page(10, 'text'),
    #     ]

    layout = Layout(DATA, WIDTH, HEIGHT)
    layout.show_window()
    print 'hoge'
