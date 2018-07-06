import unittest

import lot

class TestCar(unittest.TestCase):
    def test_plate_no_transform(self):
        car = lot.Car("axs0989", "matte black")
        self.assertEqual("AXS0989", car.plate_no)

    def test_color_transform(self):
        car = lot.Car("axs0989", "matte black")
        self.assertEqual("Matte Black", car.color)

class TestTicket(unittest.TestCase):
    def test_nothing(self):
        pass

class TestLot(unittest.TestCase):
    """This should contain a lot of test methods."""
    # do you see what i did there :) ;)
    def test_build_lot(self):
        test_lot = lot.Lot(12)
        test_lot.build_lot()
        self.assertEqual(12, len(test_lot.slots))

if __name__ == "__main__":
    unittest.main()