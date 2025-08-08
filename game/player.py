class Player(object):
    def __init__(self, name):
        self.name = name
        self._lives = 1
        self._level = 1
        self.score = 0


    def _get_level(self):
        return self._level


    def _set_level(self, value):
        if value >= 0:
            self._level = value
        else:
            print("Level cannot be negative")
            self._level = 0

    level = property(_get_level, _set_level)


    def _get_lives(self):
        if self.level > 0:
            return self.level * 1000
        else:
            return 0


    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be negative")
            self._lives = 0

    lives = property(_get_lives, _set_lives)

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score {0.score}".format(self)
