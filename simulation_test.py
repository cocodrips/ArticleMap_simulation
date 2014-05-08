import unittest
import simulation
from squaretype import LayoutType, Pages
from squaretype import LayoutTypes


class SimulationTest(unittest.TestCase):
    def setUp(self):
        self.layout = simulation.Layout()
        data = {
            'image': [
                LayoutType([10], 'image'),
                LayoutType([8], 'image'),
                LayoutType([6], 'image'),
                LayoutType([4], 'image'),
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
        pages = Pages(data)
        self.layout.set_data(data)

    def testSetData(self):
        self.layout.data['image'][0].priority

    def testPrioritySum(self):
        self.assertEqual(self.layout.priority_sum(self.layout.data), 55)


    def testSetIdealArea(self):
        self.layout._set_ideal_area()
        self.assertEqual(self.layout.data['image'][0].ideal_area, 28597)
        self.assertEqual(self.layout.data['text'][0].ideal_area, 14298)

    def testArrangeTopPage(self):
        self.layout._set_ideal_area()
        target = self.layout._arrange_1(self.layout.data)
        self.assertEqual(target.rect.width, 396)
        self.assertEqual(target.rect.height, 360)



if __name__ == '__main__':
    unittest.main()
