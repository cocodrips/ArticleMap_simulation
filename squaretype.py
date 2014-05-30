# -*- coding: utf-8 -*-
IMAGE_RATIO = 1.3

class RectType:
    def __init__(self, ratio, min_align=1):
        self.ratio = ratio
        self.min_align = min_align


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
    """
    Page
    """

    rect = ''
    ideal_area = ''
    priority = 0
    type = None

    rect_types = {
        'image': [
            RectType(1.1, 1),
            RectType(0.5, 2),
            RectType(2.2, 2)],
        'text': [
            RectType(1.3, 1),
            RectType(1.6, 2)]
    }

    def __init__(self, priority, string):
        self.priority = priority
        self.type = string

    def __repr__(self):
        return unicode("<Page priority:{0}>".format(self.priority))


import itertools
class Pages:
    page_set = []

    def __init__(self, data):
        self.page_set = [[d] for d in data]
        self.page_set.sort(cmp=self.page_cmp)
        self.page_set.reverse()


    @property
    def priority_sum(self):
        return sum([sum([page.priority for page in pages]) for pages in self.page_set])

    @property
    def rest(self):
        """
        まだ高さが配置されていないデータを抽出

        Returns: Array
        """
        array = []
        for data in self.page_set.values():
            for d in data:
                if not d.rect:
                    array.append(d)
        return array

    def page_cmp(self, x, y):
        return cmp(sum([page.priority for page in x]),
                   sum([page.priority for page in y]))


    def set_ideal_area(self, width, height):
        s = self.priority_sum
        all_area = width * height

        for data in self.page_set.values():
            for d in data:
                d.ideal_area = sum(d.priority) * all_area // s

    def get_top_1(self):
        for t in self.types:
            if self.page_set[t]:
                return self.page_set[t][0]
        return None

    def get_optimum_set(self, rect):
        s = rect.width * rect.height
        candidate = None
        max_length = max([len(self.page_set[t]) for t in self.types])
        num = 1
        while not candidate and num < max_length:
            for t in self.types:
                if num < len(self.page_set[t]):
                    candidate = self._create_sets(self.page_set[t], num, s)
            num += 1

        if not candidate:
            self.get_top_1()
        return candidate

    def _create_sets(self, data, num, s):
        """
        面積Sに対して、
        １番適した面積を探す
        TODO:擬多項式時間
        """

        candidate = None
        candidate_area = 100000000000
        combinations = itertools.combinations(data, num)

        for combination in combinations:
            area_sum = sum([c.ideal_area for c in combination])

            if not candidate and area_sum < s:
                return candidate

            if area_sum >= s:
                if area_sum - s < candidate_area - s:
                    candidate = combination
                    candidate_area = area_sum

        return candidate
