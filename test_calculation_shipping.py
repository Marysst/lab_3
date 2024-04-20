import unittest
from calculation_shipping import GroundShipping, AirShipping, SeaShipping

class TestShippingMethods(unittest.TestCase):

    def test_ground_shipping_cost_normal(self):
        ground_shipping = GroundShipping(width=1, length=1, height=1, weight=10, distance=10000, shipping_type='normal')
        self.assertAlmostEqual(ground_shipping.calculate_cost(), 1015.5, delta=0.01)

    def test_ground_shipping_time_normal(self):
        ground_shipping = GroundShipping(width=1, length=1, height=1, weight=10, distance=10000, shipping_type='normal')
        self.assertAlmostEqual(ground_shipping.calculate_time(), 83.33, delta=0.01)

    def test_ground_shipping_cost_fast(self):
        ground_shipping = GroundShipping(width=1, length=1, height=1, weight=10, distance=10000, shipping_type='fast')
        self.assertAlmostEqual(ground_shipping.calculate_cost(), 2031.0, delta=0.01)

    def test_ground_shipping_time_fast(self):
        ground_shipping = GroundShipping(width=1, length=1, height=1, weight=10, distance=10000, shipping_type='fast')
        self.assertAlmostEqual(ground_shipping.calculate_time(), 41.66, delta=0.01)

    def test_air_shipping_cost_normal(self):
        air_shipping = AirShipping(width=1, length=1, height=1, weight=10, distance=10000, shipping_type='normal')
        self.assertAlmostEqual(air_shipping.calculate_cost(), 10051.0, delta=0.01)

    def test_air_shipping_time_normal(self):
        air_shipping = AirShipping(width=1, length=1, height=1, weight=10, distance=10000, shipping_type='normal')
        self.assertAlmostEqual(air_shipping.calculate_time(), 12.5, delta=0.01)

    def test_air_shipping_cost_fast(self):
        air_shipping = AirShipping(width=1, length=1, height=1, weight=10, distance=10000, shipping_type='fast')
        self.assertAlmostEqual(air_shipping.calculate_cost(), 20102.0, delta=0.01)

    def test_air_shipping_time_fast(self):
        air_shipping = AirShipping(width=1, length=1, height=1, weight=10, distance=10000, shipping_type='fast')
        self.assertAlmostEqual(air_shipping.calculate_time(), 6.25, delta=0.01)

    def test_sea_shipping_cost_normal(self):
        sea_shipping = SeaShipping(width=1, length=1, height=1, weight=10, distance=10000, shipping_type='normal')
        self.assertAlmostEqual(sea_shipping.calculate_cost(), 5020.3, delta=0.01)

    def test_sea_shipping_time_normal(self):
        sea_shipping = SeaShipping(width=1, length=1, height=1, weight=10, distance=10000, shipping_type='normal')
        self.assertAlmostEqual(sea_shipping.calculate_time(), 22.22, delta=0.01)

    def test_sea_shipping_cost_fast(self):
        sea_shipping = SeaShipping(width=1, length=1, height=1, weight=10, distance=10000, shipping_type='fast')
        self.assertAlmostEqual(sea_shipping.calculate_cost(), 10040.6, delta=0.01)

    def test_sea_shipping_time_fast(self):
        sea_shipping = SeaShipping(width=1, length=1, height=1, weight=10, distance=10000, shipping_type='fast')
        self.assertAlmostEqual(sea_shipping.calculate_time(), 11.11, delta=0.01)

if __name__ == '__main__':
    unittest.main()
