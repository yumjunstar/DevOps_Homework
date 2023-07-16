import os
import unittest
from unittest import TestCase
from calculation import CalculationService
import random
class Test_cal_service(TestCase):
    # def __init__ (self):
    #     super().__init__()
    #     self.a = None
    #     self.b = None
    input_paths = "data/input.txt"
    output_paths = "../share_dir/output.txt"
    def set_test_range(self):
        self.a = random.sample(range(0, int(1E10)), 1000)
        self.b = random.sample(range(0, int(1E10)), 1000)
    # 반드시 test로 시작해야 됨
    def test_multiply(self):
        self.set_test_range()
        cal = CalculationService(input_path= self.input_paths, output_path = self.output_paths)
        cal.generate_data(100)
        for i, j in zip (self.a, self.b):
            target = i + j
            self.assertEqual(cal.add(i, j), target)
        cal.load_data()
        cal.process_data()
    def test_addition(self):
        self.set_test_range()

        cal = CalculationService(input_path= self.input_paths, output_path = self.output_paths)
        cal.generate_data(100)
        for i, j in zip (self.a, self.b):
            target = i * j
            self.assertEqual(cal.mul(i, j), target)
        cal.load_data()
        cal.process_data()
    def test_division(self):
        self.set_test_range()

        cal = CalculationService(input_path= self.input_paths, output_path = self.output_paths)
        cal.generate_data(100)
        for i, j in zip (self.a, self.b):
            target = i / j
            self.assertEqual(cal.div(i, j), target)
        cal.load_data()
        cal.process_data()

if __name__ == "__main__":
    test_a = random.sample(range(0, int(1E10)), 50)
    test_b = random.sample(range(0, int(1E10)), 50)
    
    ins = Test_cal_service()
    # ins.set_test_range(test_a, test_b)
    unittest.main()