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
        self.assertEqual(pages.priority_sum(self.page_sets[0] + self.page_sets[1]), 19)


    def testSetIdealArea(self):
        self.assertEqual(self.page_sets[0][0].ideal_area, 1818)
        self.assertEqual(self.page_sets[-1][0].ideal_area, 181)
        target = [self.page_sets[i][0].ideal_area for i in xrange(10)]
        expected = [1818, 1636, 1454, 1272, 1090, 909, 727, 545, 363, 181]
        self.assertEqual(target, expected)

    def testGroupingPageSet(self):
        self.page_sets = pages.grouping_page_sets(self.page_sets)
        self.assertEqual(len(self.page_sets), 4)

    def testGetTop1(self):
        target = pages.get_top_1(self.page_sets)
        self.assertEqual(pages.priority_sum(target), 10)

        page_sets = pages.grouping_page_sets(self.page_sets)
        target = pages.get_top_1(page_sets)
        self.assertEqual(pages.priority_sum(target), 18)

    def testGetOptimumSet(self):
        target = pages.get_optimum_set(self.page_sets, Rect(0, 0, 20, 20))
        self.assertEqual(pages.priority_sum(target), 2)
        self.page_sets = pages.grouping_page_sets(self.page_sets)
        target = pages.get_optimum_set(self.page_sets, Rect(0, 0, 50, 50))
        self.assertEqual(pages.priority_sum(target), 12)


WIDTH = 1024
HEIGHT = 768


class SimulationTest(unittest.TestCase):
    def setUp(self):
        self.layout = simulation.Layout(DATA, WIDTH, HEIGHT)
        self.page_sets = pages.init(DATA, WIDTH, HEIGHT)
        self.rect = Rect(0, 0, WIDTH, HEIGHT)

    def testSetData(self):
        target = self.layout.page_sets[0][0].priority
        self.assertEqual(target, 10)

    def testArrangeTopPage(self):
        self.layout._arrange(self.page_sets, self.rect)
        top = self.page_sets[0][0]
        self.assertEqual((top.rect.width, top.rect.height),
                         (396, 360))

    def testArrangeVertical(self):
        pass
        # page_sets = [Page(4, 'image'), Page(8, 'image'), Page(6, 'image')]
        # self.layout.arrange_vertical(page_sets, Rect(0,0, 300, 100))
        # self.assertEqual(page_sets[1].rect.vec4(), (100, 0, 100, 100))
        #
        # #group
        # page_sets = [Page(4, 'image'), Page(6, 'image'), Page(8, 'image'),Page(10, 'image')]
        # page_sets = pages.init(page_sets, WIDTH, HEIGHT)
        # page_sets = pages.grouping_page_sets(page_sets)
        # self.layout.arrange_vertical(page_sets, Rect(0,0, 300, 100))
        # self.assertEqual(page_sets[0][1].rect.vec4(), (75, 0, 75, 100))

    def testArrangeHorizontal(self):
        page_sets = [Page(4, 'image'), Page(8, 'image'), Page(6, 'image')]
        self.layout.arrange_horizontal(page_sets, Rect(0,0, 100, 300))
        # self.assertEqual(page_sets[1].rect.vec4(), (0, 100, 100, 100))
        for pages in page_sets:
            print pages.rect






if __name__ == '__main__':
    unittest.main()
