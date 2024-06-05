import unittest
import coverage
from tests.test_restaurant_day import TestRestaurantDay

if __name__ == '__main__':
    cov = coverage.Coverage()
    cov.start()
    unittest.main()
    cov.stop()
    cov.save()
    cov.report()
