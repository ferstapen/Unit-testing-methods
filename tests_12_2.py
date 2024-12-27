import runner_and_tournament
import unittest

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        TournamentTest.all_results = {}

    def setUp(self):
        self.usein = runner_and_tournament.Runner('Усэйн', 10)
        self.andre = runner_and_tournament.Runner('Андрей', 9)
        self.nic = runner_and_tournament.Runner('Ник', 3)

    def testing_1(self):
        tourn_1 = runner_and_tournament.Tournament(90, self.usein, self.nic)
        TournamentTest.all_results = tourn_1.start()
        self.assertTrue(TournamentTest.all_results[2], 'Ник')

    def testing_2(self):
        tourn_2 = runner_and_tournament.Tournament(90, self.andre, self.nic)
        TournamentTest.all_results = tourn_2.start()
        self.assertTrue(TournamentTest.all_results[2], 'Ник')

    def testing_3(self):
        tourn_3 = runner_and_tournament.Tournament(90, self.usein, self.andre, self.nic)
        TournamentTest.all_results = tourn_3.start()
        self.assertTrue(TournamentTest.all_results[2], 'Ник')

    @classmethod
    def tearDowmClass(cls):
        for key, value in TournamentTest.all_results.items():
            print(f'{key} - {value}')

if __name__ == '__main__':
    unittest.main()
