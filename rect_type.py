class RectType:
    def __init__(self, ratio, min_align=1):
        self.ratio = ratio
        self.min_align = min_align

rect_types = {
    'image': [
        RectType(1.1, 1),
        RectType(0.5, 2),
        RectType(2.2, 2)
        # RectType(0.8, 1),
        ],
    'text': [
        RectType(1.3, 1),
        RectType(1.6, 1)
    ]
}