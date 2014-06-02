# -*- coding: utf-8 -*-
import unittest
import simulation
import pages
from squaretype import Page, Rect

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


class PagesTest(unittest.TestCase):
    def setUp(self):
        self.page_sets = pages.init(DATA, 100, 100)

    def testInit(self):
        self.assertEqual(self.page_sets[0][0].priority, 10)
        self.assertEqual(self.page_sets[-1][0].priority, 1)

    def testPrioritySum(self):
        self.assertEqual(pages.priority_sum(self.page_sets[0]), 10)

    def testSetIdealArea(self):
        self.assertEqual(self.page_sets[0][0].ideal_area, 1818)
        self.assertEqual(self.page_sets[-1][0].ideal_area, 181)
        target = [self.page_sets[i][0].ideal_area for i in xrange(10)]
        expected = [1818, 1636, 1454, 1272, 1090, 909, 727, 545, 363, 181]
        self.assertEqual(target, expected)

    def testGetTop1(self):
        target = pages.get_top_1(self.page_sets)
        self.assertEqual(pages.priority_sum(target), 10)

    def testGroupingPageSet(self):
        self.page_sets = pages.grouping_page_sets(self.page_sets)
        self.assertEqual(len(self.page_sets), 4)

    def testGetOptimumSet(self):
        target = pages.get_optimum_set(self.page_sets,Rect(0, 0, 20, 20))
        self.assertEqual(pages.priority_sum(target), 2)
        self.page_sets = pages.grouping_page_sets(self.page_sets)
        target = pages.get_optimum_set(self.page_sets, Rect(0, 0, 50, 50))
        self.assertEqual(pages.priority_sum(target), 12)

WIDTH = 1024
HEIGHT = 768

class SimulationTest(unittest.TestCase):

    def setUp(self):
        self.layout = simulation.Layout(DATA)

    def testSetData(self):
        target = self.layout.page_sets[0][0].priority
        self.assertEqual(target, 10)

#     def testArrangeTopPage(self):
#         self.layout._set_ideal_area()
#         target = self.layout._arrange_1(self.layout.data)
#         self.assertEqual(target.rect.width, 396)
#         self.assertEqual(target.rect.height, 360)






if __name__ == '__main__':
    unittest.main()
