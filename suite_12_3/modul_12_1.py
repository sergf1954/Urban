import unittest




class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    is_frozen = False
    def setUp(self):
        self.first = Runner('first')
        self.second = Runner('second')

    @unittest.skipIf(is_frozen, 'Тесты в этом кэйсе заморожены')
    def test_walk(self):
        for _ in range(10):
            self.first.walk()
        self.assertEqual(self.first.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кэйсе заморожены')
    def test_run(self):
        for _ in range(10):
            self.first.run()
        self.assertEqual(self.first.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кэйсе заморожены')
    def test_challenge(self):
        for _ in range(10):
            self.first.walk()
            self.second.run()
        self.assertNotEqual(self.first.distance,self.second.distance)

if __name__ == "__main__":
    unittest.main()


