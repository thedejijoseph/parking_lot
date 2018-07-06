import unittest

import lot

class TestCar(unittest.TestCase):
    def test_plate_no_transform(self):
        car = lot.Car("axs0989", "matte black")
        self.assertEqual("AXS0989", car.plate_no)
    
    def test_color_transform(self):
        car = lot.Car("axs0989", "matte black")
        self.assertEqual("Matte Black", car.color)

if __name__ == "__main__":
    unittest.main()