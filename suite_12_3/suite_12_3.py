import unittest
import modul_12_1
import modul_12_2

test_13_2 = unittest.TestSuite()

test_13_2.addTest(unittest.TestLoader().loadTestsFromTestCase(modul_12_1.RunnerTest))
test_13_2.addTest(unittest.TestLoader().loadTestsFromTestCase(modul_12_2.TournamentTest))


runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_13_2)