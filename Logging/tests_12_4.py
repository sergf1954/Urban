import unittest
import logging

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_test.log', encoding="utf-8",
                    format="%(asctime)s | %(levelname)s | %(message)s")



class Runner:
    def __init__(self, name = None, speed=5):
        #if isinstance(name, str):
        if name == None:
           self.name = ''
        else:
            self.name = name
        # else:
        #     raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        #if speed > 0:
        self.speed = speed
        #else:
        #    raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def walk(self):
        self.distance += self.speed

    def run(self):
        self.distance += self.speed * 2


    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class RunnerTest(unittest.TestCase):
    is_frozen = False
    def setUp(self):
        self.first = Runner('First',5)
        #self.first = Runner('', -5)
        self.second = Runner('Second', 6)


    @unittest.skipIf(is_frozen, 'Тесты в этом кэйсе заморожены')
    def test_walk(self):
        try:
            if self.first.speed > 0:
                logging.info('"test_walk"  выполнен успешно')
                for _ in range(10):
                    self.first.walk()
                self.assertEqual(self.first.distance, 50)
            else:
                raise ValueError
        except ValueError:
            logging.warning(f'Скорость не может быть отрицательной, сейчас {self.first.speed}')


    @unittest.skipIf(is_frozen, 'Тесты в этом кэйсе заморожены')
    def test_run(self):
        try:
            if isinstance(self.first.name, str) and self.first.name != '':
                logging.info('"test_run"  выполнен успешно')
                for _ in range(10):
                    self.first.run()
                self.assertEqual(self.first.distance, 100)
            else:
                raise TypeError
        except TypeError :
            logging.warning(f'"test_run" Имя может быть только строкой, передано {self.first.name}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кэйсе заморожены')
    def test_challenge(self):
        for _ in range(10):
            self.first.walk()
            self.second.run()
        self.assertNotEqual(self.first.distance,self.second.distance)

if __name__ == "__main__":
    unittest.main()




