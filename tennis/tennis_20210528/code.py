
class State:
    pass

class NormalState(State):
    def __init__(self, player1_score, player2_score) -> None:
        self.player1_score = player1_score
        self.player2_score = player2_score

    def score(self):
        score_mapping = {
            0: 'Love',
            1: 'Fifteen',
            2: 'Thirty',
            3: 'Forty',
        }
        return f'{score_mapping[self.player1_score]} {score_mapping[self.player2_score]}'


class DeuceState(State):
    pass


class AdvantageState(State):
    pass


class TennisGame:
    def __init__(self):
        self.state = NormalState(player1_score=0, player2_score=0)

    def player1_score(self):
        s = self.state
        if isinstance(s, NormalState):
            self.state = NormalState(s.player1_score + 1, s.player2_score)

    def player2_score(self):
        s = self.state
        if isinstance(s, NormalState):
            self.state = NormalState(s.player1_score, s.player2_score + 1)

    def score(self):
        return self.state.score()


        # if self._in_deuce_state():
        #     return self._deuce_score()
        #
        # if self._in_game_over_state():
        #     return self._game_over_score()
        #
        # return self._in_game_score()

    # def _in_deuce_state(self):
    #     return self._player1_score >= 3 and self._player2_score >= 3
    #
    # def _deuce_score(self):
    #     if self._player1_score == self._player2_score:
    #         return 'deuce'
    #
    #     player = 1 if self._player1_score > self._player2_score else 2
    #     distance = abs(self._player1_score - self._player2_score)
    #
    #     if distance == 1:
    #         return f'player{player} advantage'
    #     if distance == 2:
    #         return f'player{player} win'
    #
    # def _in_game_over_state(self):
    #     return self._player1_score == 4 or self._player2_score == 4
    #
    # def _game_over_score(self):
    #     player = 1 if self._player1_score > self._player2_score else 2
    #     return f'player{player} win'
    #
    # def _in_game_score(self):
    #     score_mapping = {
    #         0: 'Love',
    #         1: 'Fifteen',
    #         2: 'Thirty',
    #         3: 'Forty',
    #     }
    #     return f'{score_mapping[self._player1_score]} {score_mapping[self._player2_score]}'
