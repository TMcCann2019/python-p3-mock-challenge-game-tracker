class Game:

    all_games = []

    def __init__(self, title):
        self.title = title
        self.all_games.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not hasattr(self, '_title') and isinstance (value, str) and len(value) > 0:
            self._title = value
        else:
            raise Exception('Title must be a non-empty string and cannot be changed')

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list(set(result.player for result in self.results()))

    def average_score(self, player):
        player_results = [result.score for result in self.results() if result.player == player]
        if player_results:
            return sum(player_results) / len(player_results)
        else:
            return 0

class Player:
    all_players = []

    def __init__(self, username):
        self.username = username
        self.all_players.append(self)

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, value):
        if isinstance(value, str) and (len(value) > 1 and len(value) < 17):
            self._username = value
        else:
            raise Exception('Username must be a non-empty string between 2 and 16 characters')

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return list(set(result.game for result in self.results()))

    def played_game(self, game):
        return any(result.game == game for result in self.results())

    def num_times_played(self, game):
        return sum(1 for result in self.results() if result.game == game)
    
    @classmethod
    def highest_scored(cls, game):
        players = [player for player in cls.all_players if player.played_game(game)]
        if not players:
            return None
        
        game.average_score(cls.all_players)
        # def average_score(player):
        #     player_results = [result.score for result in game.results() if result.player == player]
        #     return sum(player_results) / len(player_results)
        
        return max(players, key= lambda player: game.average_score(player))

class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        self.all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        if not hasattr(self, "_score") and isinstance(value, int) and (1 <= value <= 5000):
            self._score = value
        else:
            raise Exception('Score must be an integer between 1 and 5000')
        
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, value):
        if not isinstance(value, Player):
            raise Exception('Player must be of type Player')
        else:
            self._player = value

    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, value):
        if not isinstance(value, Game):
            raise Exception('Game must be of type Game')
        else:
            self._game = value