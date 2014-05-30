import unittest
import simulation
from squaretype import Page, Pages, Rect

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
        self.pages = Pages(DATA)

    def testSort(self):
        self.assertEqual(self.pages.page_sets[0][0].priority, 10)
        self.assertEqual(self.pages.page_sets[-1][0].priority, 1)

    def testPrioritySum(self):
        self.assertEqual(self.pages.priority_sum(self.pages.page_sets[0]), 10)

    def testSetIdealArea(self):
        self.pages.set_ideal_area(100, 100)
        self.assertEqual(self.pages.page_sets[0][0].ideal_area, 1818)
        self.assertEqual(self.pages.page_sets[-1][0].ideal_area, 181)
        target = [self.pages.page_sets[i][0].ideal_area for i in xrange(10)]
        expected = [1818, 1636, 1454, 1272, 1090, 909, 727, 545, 363, 181]
        self.assertEqual(target, expected)

    def testGetTop1(self):
        target = self.pages.get_top_1()
        self.assertEqual(self.pages.priority_sum(target), 10)

    def testGroupingPageSet(self):
        self.pages.grouping_page_sets()
        print self.pages.page_sets
        self.assertEqual(len(self.pages.page_sets), 4)

    def testGetOptimumSet(self):
        self.pages.set_ideal_area(100,100)
        target = self.pages.get_optimum_set(Rect(0, 0, 20, 20))
        self.assertEqual(self.pages.priority_sum(target), 2)

        self.pages.grouping_page_sets()
        target = self.pages.get_optimum_set(Rect(0, 0, 50, 50))
        self.assertEqual(self.pages.priority_sum(target), 12)


class SimulationTest(unittest.TestCase):
    def setUp(self):
        pass
    #     pages = Pages(DATA)
    #     self.layout = simulation.Layout(pages)
    #
    # def testSetData(self):
    #     target = self.layout.pages.data['image'][0].priorities
    #     self.assertEqual(target, [10])


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
