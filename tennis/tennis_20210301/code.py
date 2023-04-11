class TennisGame(object):
    def __init__(self, name1, name2):
        self._name1 = name1
        self._name2 = name2
        self._score_one = 0
        self._score_two = 0

    def score(self):
        score_lookup = {
            0: 'Love',
            1: 'Fifteen',
            2: 'Thirty',
            3: 'Forty',
        }

        if self._score_one == self._score_two:
            if self._score_one >= 3:
                return 'Deuce'

            return f'{score_lookup[self._score_one]} All'

        if self._score_one >= 4 or self._score_two >= 4:
            distance = abs(self._score_one - self._score_two)

            if distance == 1:
                winner = self._name1 if self._score_one == 4 else self._name2
                return f'{winner} Adv'

            if distance == 2:
                winner = self._name1 if self._score_one == 4 else self._name2
                return f'{winner} Win'

        return f'{score_lookup[self._score_one]} {score_lookup[self._score_two]}'

    def player_one_score(self):
        self._score_one += 1

    def player_two_score(self):
        self._score_two += 1
