import pytest

from tennis_20210528.code import TennisGame

"""
https://codingdojo.org/kata/Tennis/
"""


class TestTennisGame:
    def setup_method(self):
        self.game = TennisGame()

    def assert_p1_score_get(self, score):
        self.game.player1_score()
        assert self.game.score() == score

    def assert_p2_score_get(self, score):
        self.game.player2_score()
        assert self.game.score() == score

    def test_game_before_start(self):
        assert self.game.score() == 'Love Love'

    def test_player1_all_win(self):
        self.assert_p1_score_get('Fifteen Love')
        self.assert_p1_score_get('Thirty Love')
        self.assert_p1_score_get('Forty Love')
        self.assert_p1_score_get('player1 win')

    def test_player2_all_win(self):
        self.assert_p2_score_get('Love Fifteen')
        self.assert_p2_score_get('Love Thirty')
        self.assert_p2_score_get('Love Forty')
        self.assert_p2_score_get('player2 win')

    def test_player1_advantage_and_win(self):
        self.assert_p1_score_get('Fifteen Love')
        self.assert_p1_score_get('Thirty Love')
        self.assert_p1_score_get('Forty Love')
        self.assert_p2_score_get('Forty Fifteen')
        self.assert_p2_score_get('Forty Thirty')
        self.assert_p2_score_get('deuce')
        self.assert_p1_score_get('player1 advantage')
        self.assert_p2_score_get('deuce')
        self.assert_p2_score_get('player2 advantage')
        self.assert_p1_score_get('deuce')
        self.assert_p1_score_get('player1 advantage')
        self.assert_p1_score_get('player1 win')

    def test_player2_advantage_and_win(self):
        self.assert_p2_score_get('Love Fifteen')
        self.assert_p2_score_get('Love Thirty')
        self.assert_p2_score_get('Love Forty')
        self.assert_p1_score_get('Fifteen Forty')
        self.assert_p1_score_get('Thirty Forty')
        self.assert_p1_score_get('deuce')
        self.assert_p2_score_get('player2 advantage')
        self.assert_p1_score_get('deuce')
        self.assert_p1_score_get('player1 advantage')
        self.assert_p2_score_get('deuce')
        self.assert_p2_score_get('player2 advantage')
        self.assert_p2_score_get('player2 win')
