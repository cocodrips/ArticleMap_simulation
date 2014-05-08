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
        self.priorities = [priorities]
        self.type = string
        self.rect_type = LayoutTypes().rect_types[string]


class Pages:
    types = LayoutType().types
    data = {}

    def __init__(self, dict):
        for t in self.types:
            self.data[t] = dict[t]
            self.sort(self.data[t])

    def priority_sum(self):
        sum = 0
        for data in self.data.values():
            for d in data:
                sum += d.priority
        return sum

    def sort(self, page_set):
        page_set.sort(cmp=lambda x, y: cmp(x.priority, y.priority))


    def set_ideal_area(self, width, height):
        s = self.priority_sum(self.data)
        all_area = width, height

        for data in self.data.values():
            for d in data:
                d.ideal_area = d.priority * all_area // s

    def get_top_1(self):
        pass

    def get_optimum_set(self):
        pass


