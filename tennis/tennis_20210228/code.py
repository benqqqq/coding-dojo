class TennisGame(object):
    score_map = {
        0: 'Love',
        1: 'Fifteen',
        2: 'Thirty',
        3: 'Forty',
    }

    def __init__(self, player_one_name, player_two_name) -> None:
        super().__init__()

        self.player_one_name = player_one_name
        self.player_two_name = player_two_name
        self.player_one_score = None
        self.player_two_score = None

    def set_player_one_score(self, score):
        self.player_one_score = score

    def set_player_two_score(self, score):
        self.player_two_score = score

    def score(self):
        if self.player_one_score == self.player_two_score:
            score = self.player_one_score

            if score >= 3:
                return 'Deuce'
            else:
                return f'{self.score_map[score]} All'

        if self.player_one_score >= 5:
            return f'{self.player_one_name} Win'

        if self.player_two_score >= 5:
            return f'{self.player_two_name} Win'

        if self.player_one_score >= 4:
            return f'{self.player_one_name} Adv'

        if self.player_two_score >= 4:
            return f'{self.player_two_name} Adv'

        return ' '.join(
            [
                self.score_map[self.player_one_score],
                self.score_map[self.player_two_score],
            ]
        )
