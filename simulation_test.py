import unittest
import simulation
from squaretype import LayoutType, Pages, Rect
from squaretype import LayoutTypes


DATA = {
    'image': [
        LayoutType([4], 'image'),
        LayoutType([8], 'image'),
        LayoutType([6], 'image'),
        LayoutType([10], 'image'),
        LayoutType([2], 'image'),
    ],
    'text': [
        LayoutType([9], 'text'),
        LayoutType([7], 'text'),
        LayoutType([5], 'text'),
        LayoutType([3], 'text'),
        LayoutType([1], 'text'),
    ]
}

class PagesTest(unittest.TestCase):
    def setUp(self):
        self.pages = Pages(DATA)

    def testSort(self):
        self.assertEqual(self.pages.data['image'][0].priorities, [10])
        self.assertEqual(self.pages.data['text'][-1].priorities, [1])

    def testSetIdealArea(self):
        self.pages.set_ideal_area(100, 100)
        self.assertEqual(self.pages.data['image'][0].ideal_area, 1818)
        self.assertEqual(self.pages.data['text'][-1].ideal_area, 181)
        # for data in self.pages.data.values():
        #     for d in data:
        #         print d.priorities, d.ideal_area

    def testGetTop1(self):
        target = self.pages.get_top_1()
        self.assertEqual(target.priorities, [10])

    def testGetOptimumSet(self):
        self.pages.set_ideal_area(100,100)
        target = self.pages.get_optimum_set(Rect(0, 0, 20, 20))
        self.assertEqual(target[0].priorities, [3])
        target = self.pages.get_optimum_set(Rect(0, 0, 50, 70))
        self.assertEqual([t.priorities for t in target], [[9], [7], [5]])




# class SimulationTest(unittest.TestCase):
#     def setUp(self):
#         self.layout = simulation.Layout()
#         data = {
#             'image': [
#                 LayoutTyp([10], 'image'),
#                 LayoutType([8], 'image'),
#                 LayoutType([6], 'image'),
#                 LayoutType([4], 'image'),
#                 LayoutType([2], 'image'),
#             ],
#             'text': [
#                 LayoutType([9], 'text'),
#                 LayoutType([7], 'text'),
#                 LayoutType([5], 'text'),
#                 LayoutType([3], 'text'),
#                 LayoutType([1], 'text'),
#             ]
#
#         }
#         pages = Pages(data)
#         self.layout.set_data(data)
#
#     def testSetData(self):
#         self.layout.data['image'][0].priority
#
#     def testPrioritySum(self):
#         self.assertEqual(self.layout.priority_sum(self.layout.data), 55)
#
#
#     def testSetIdealArea(self):
#         self.layout._set_ideal_area()
#         self.assertEqual(self.layout.data['image'][0].ideal_area, 28597)
#         self.assertEqual(self.layout.data['text'][0].ideal_area, 14298)
#
#     def testArrangeTopPage(self):
#         self.layout._set_ideal_area()
#         target = self.layout._arrange_1(self.layout.data)
#         self.assertEqual(target.rect.width, 396)
#         self.assertEqual(target.rect.height, 360)






if __name__ == '__main__':
    unittest.main()
