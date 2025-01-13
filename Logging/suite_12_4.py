import unittest
import tests_12_4


test_13_2 = unittest.TestSuite()


test_13_2.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_4.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_13_2)