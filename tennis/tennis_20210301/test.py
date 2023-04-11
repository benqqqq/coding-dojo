import pytest

from tennis_20210301.code import TennisGame


@pytest.mark.parametrize(
    'player_one_score, player_two_score, expected',
    [
        (0, 0, 'Love All'),
        (0, 1, 'Love Fifteen'),
        (1, 0, 'Fifteen Love'),
        (2, 0, 'Thirty Love'),
        (3, 0, 'Forty Love'),
        (4, 0, 'Liz Adv'),
        (0, 4, 'Dz Adv'),
        (1, 1, 'Fifteen All'),
        (2, 2, 'Thirty All'),
        (3, 3, 'Deuce'),
        (4, 4, 'Deuce'),
        (5, 5, 'Deuce'),
        (7, 5, 'Liz Win'),
    ]
)
def test_tennis_game(player_one_score, player_two_score, expected):
    game = TennisGame('Liz', 'Dz')

    for _ in range(0, player_one_score):
        game.player_one_score()
    for _ in range(0, player_two_score):
        game.player_two_score()

    assert game.score() == expected
