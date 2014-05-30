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
        print [page for page in self.pages.page_set]
        self.assertEqual(self.pages.page_set[0][0].priority, 10)
        self.assertEqual(self.pages.page_set[-1][0].priority, 1)

    # def testSetIdealArea(self):
    #     self.pages.set_ideal_area(100, 100)
    #     self.assertEqual(self.pages.page_set['image'][0].ideal_area, 1818)
    #     self.assertEqual(self.pages.page_set['text'][-1].ideal_area, 181)
    #     # for data in self.pages.data.values():
    #     #     for d in data:
    #     #         print d.priorities, d.ideal_area
    #
    # def testGetTop1(self):
    #     target = self.pages.get_top_1()
    #     self.assertEqual(target.priorities, [10])
    #
    # def testGetOptimumSet(self):
    #     self.pages.set_ideal_area(100,100)
    #     target = self.pages.get_optimum_set(Rect(0, 0, 20, 20))
    #     self.assertEqual(target[0].priorities, [3])
    #     target = self.pages.get_optimum_set(Rect(0, 0, 50, 70))
    #     self.assertEqual([t.priorities for t in target], [[9], [7], [5]])
    #
    # def testGetRest(self):
    #     print self.pages.get_rest()




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
