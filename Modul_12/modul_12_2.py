import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
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

    # def start(self):
    #     finishers = {}
    #     place = 1
    #     while self.participants:
    #         for participant in self.participants:
    #             participant.run()
    #             if participant.distance >= self.full_distance:
    #                 finishers[place] = participant
    #                 place += 1
    #                 self.participants.remove(participant)
    #
    #     return finishers


    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                finishers[self.full_distance/participant.distance] = participant
                place += 1
                self.participants.remove(participant)
        sorted_tuple = dict(sorted(finishers.items(), key=lambda x: x[0]))
        k = 1
        finishers = {}
        for i in sorted_tuple:
            finishers[k] = sorted_tuple[i]
            k += 1
        return finishers


class TournamentTest(unittest.TestCase):
    def setUp(self):
        self.usain = Runner('Усэйн', 10)
        self.andrey = Runner('Андрей', 9)
        self.nick = Runner('Ник', 3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
    @classmethod
    def tearDownClass(cls):
        result = {}
        for i in cls.all_results:
            for j in range(len(cls.all_results[i])):
                result.update({j+1:cls.all_results[i][j+1].name})
            print(result)

    def test_start_1(self):
        tournament = Tournament(90,self.usain, self.nick)
        result = tournament.start()
        self.all_results.update({1: result})
        self.assertTrue(result.get(list(result.keys())[-1]), self.nick)

    def test_start_2(self):
        tournament = Tournament(90, self.andrey, self.nick)
        result = tournament.start()
        self.all_results.update({2: result})
        self.assertTrue(result.get(list(result.keys())[-1]), self.nick)

    def test_start_3(self):
        tournament = Tournament(1, self.usain, self.andrey,  self.nick )
        result = tournament.start()
        self.all_results.update({3 : result})
        self.assertTrue(result.get(list(result.keys())[-1]), self.nick)



if __name__ == "__main__":
    unittest.main()

