# -*- coding: utf-8 -*-
from rect_type import rect_types

IMAGE_RATIO = 1.3


class Rect:
    x = 0
    y = 0
    width = 0
    height = 0

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


class Page:
    rect = None
    ideal_area = 0
    priority = 0
    type = None

    def __init__(self, priority, string):
        self.priority = priority
        self.type = string

    def __repr__(self):
        return unicode("<Page priority:{0}>".format(self.priority))


class Pages:
    page_sets = []
    fixed_pages = []

    def __init__(self, data):
        self.page_sets = [[d] for d in data]
        self.page_sets.sort(cmp=self.page_cmp)
        self.page_sets.reverse()

    def priority_sum(self, page_set):
        return sum([page.priority for page in page_set])

    def page_cmp(self, x, y):
        return cmp(sum([page.priority for page in x]),
                   sum([page.priority for page in y]))

    def fix(self, page):
        """
        Fixed pages set in fixed_pages[] from page_sets[]
        """
        pass

    def get_top_1(self):
        """
        Get page_set which have the highest priority
        """
        top = None
        for page_set in self.page_sets:
            if not top or self.priority_sum(top) < self.priority_sum(page_set):
                top = page_set
        return top

    def get_optimum_set(self, rect):
        # TODO: 組み合わせも可にする
        s = rect.width * rect.height

        match = 0
        optimum_set = None
        for page_set in self.page_sets:
            area_sum = sum([page.ideal_area for page in page_set])
            if not optimum_set or abs(s - area_sum) < abs(s - match):
                optimum_set = page_set
                match = area_sum
        return optimum_set

    # 1
    def set_ideal_area(self, width, height):
        total_priority = sum([self.priority_sum(page_set)
                              for page_set in self.page_sets])
        all_area = width * height

        for page_set in self.page_sets:
            for page in page_set:
                page.ideal_area = page.priority * all_area // total_priority

    def grouping_page_sets(self):
        """
        Create groups [1,2,3,4,5] -> [[1,2,3][4,5]]
        """
        groups = []
        for key in rect_types.keys():
            pages = [page_set for page_set in self.page_sets if page_set[0].type == key]

            if len(pages) < 2:
                # TODO: typeのpagesの数が2以下の場合どうする？
                groups.append(pages)
                continue

            for i in xrange(0, len(pages), 2):
                if i + 1 < len(pages):
                    groups.append(pages[i] + pages[i+1])
                else:
                    groups[-1] += pages[i]
        self.page_sets = groups
