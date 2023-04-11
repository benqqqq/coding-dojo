from code import TennisGame


def _create_game():
    return TennisGame('Liz', 'Dz')


def test_love_all():
    game = _create_game()
    game.set_player_one_score(0)
    game.set_player_two_score(0)
    assert game.score() == 'Love All'


def test_fifteen_love():
    game = _create_game()
    game.set_player_one_score(1)
    game.set_player_two_score(0)
    assert game.score() == 'Fifteen Love'


def test_fifteen_all():
    game = _create_game()
    game.set_player_one_score(1)
    game.set_player_two_score(1)
    assert game.score() == 'Fifteen All'


def test_thirty_love():
    game = _create_game()
    game.set_player_one_score(2)
    game.set_player_two_score(0)
    assert game.score() == 'Thirty Love'


def test_forty_love():
    game = _create_game()
    game.set_player_one_score(3)
    game.set_player_two_score(0)
    assert game.score() == 'Forty Love'


def test_love_fifteen():
    game = _create_game()
    game.set_player_one_score(0)
    game.set_player_two_score(1)
    assert game.score() == 'Love Fifteen'


def test_love_thirty():
    game = _create_game()
    game.set_player_one_score(0)
    game.set_player_two_score(2)
    assert game.score() == 'Love Thirty'


def test_love_forty():
    game = _create_game()
    game.set_player_one_score(0)
    game.set_player_two_score(3)
    assert game.score() == 'Love Forty'


def test_forty_deuce():
    game = _create_game()
    game.set_player_one_score(3)
    game.set_player_two_score(3)
    assert game.score() == 'Deuce'


def test_deuce():
    game = _create_game()
    game.set_player_one_score(4)
    game.set_player_two_score(4)
    assert game.score() == 'Deuce'


def test_liz_adv():
    game = _create_game()
    game.set_player_one_score(4)
    game.set_player_two_score(3)
    assert game.score() == 'Liz Adv'


def test_dz_adv():
    game = _create_game()
    game.set_player_one_score(3)
    game.set_player_two_score(4)
    assert game.score() == 'Dz Adv'


def test_liz_win():
    game = _create_game()
    game.set_player_one_score(5)
    game.set_player_two_score(4)
    assert game.score() == 'Liz Win'


def test_dz_win():
    game = _create_game()
    game.set_player_one_score(4)
    game.set_player_two_score(5)
    assert game.score() == 'Dz Win'
