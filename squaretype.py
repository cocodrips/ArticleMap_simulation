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


class LayoutTypes:
    types = ['image', 'text']
    rect_types = {
        'image': [
            RectType(1.1, 1),
            RectType(0.5, 2),
            RectType(2.2, 2)],
        'text': [
            RectType(1.3, 1),
            RectType(1.6, 2)]
    }


class LayoutType:
    rect = ''
    ideal_area = ''
    vector4 = ''

    def __init__(self, priorities, string):
        self.priorities = priorities
        self.type = string
        self.rect_type = LayoutTypes().rect_types[string]


import itertools


class Pages:
    types = LayoutTypes().types
    data = {}

    def __init__(self, dict):
        for t in self.types:
            self.data[t] = dict[t]
            self.sort(self.data[t])

    @property
    def priority_sum(self):
        p_sum = 0
        for data in self.data.values():
            for d in data:
                p_sum += sum(d.priorities)
        return p_sum

    def sort(self, page_set):
        page_set.sort(cmp=lambda x, y: cmp(sum(x.priorities), sum(y.priorities)))
        page_set.reverse()

    def set_ideal_area(self, width, height):
        s = self.priority_sum
        all_area = width * height

        for data in self.data.values():
            for d in data:
                d.ideal_area = sum(d.priorities) * all_area // s

    def get_top_1(self):
        for t in self.types:
            if self.data[t]:
                return self.data[t][0]
        return None

    def get_optimum_set(self, rect):
        s = rect.width * rect.height
        candidate = None
        max_length = max([len(self.data[t]) for t in self.types])
        num = 1
        while not candidate and num < max_length:
            for t in self.types:
                if num < len(self.data[t]):
                    candidate = self._create_sets(self.data[t], num, s)
            num += 1

        if not candidate:
            self.get_top_1()
        return candidate

    def _create_sets(self, data, num, s):
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







