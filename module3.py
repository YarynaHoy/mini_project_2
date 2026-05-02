# 1
class Pokemon(object):
    attack  = 12        # The "baseline" attack,...
    defense = 10        # defense, and...
    health  = 15        # health scores for new Pokemon instances
    p_type  = "Normal"  # The "type" (like 'Normal', 'Water', 'Fire', etc.) helps determine how effective certain moves will be

    attack_boost  = 3   # When we "train", this is how much we increment our attack,...
    defense_boost = 2   # defense, and...
    health_boost  = 5   # health

    evolution_threshold = 10 # How many times we need to train before we "evolve"

    def __init__(self, name, level = 5):
        self.name  = name   # The name for this *instance*
        self._level = level # The starting level for this instance (the initial underscore signals that it is a private variable)

    @property
    def level(self): # *GETTER* for the 'level' property
        return self._level

    @level.setter
    def level(self, value): # *SETTER* for the 'level' property, ensuring that it is at least 1
        if value < 1:
            raise ValueError("Level must be greater than or equal to 1")
        self._level = value

    def train(self):
        # Increment attack, defense, and health levels
        self.attack_up()
        self.defense_up()
        self.health_up()

        self.level = self.level + 1 # Increment the level

        evolved = (self.level % self.evolution_threshold == 0) # Did we "evolve" on this step?

        return self.level, evolved # Return a tuple with the current level and whether we evolved

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def __str__(self):
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

class Grass_Pokemon(Pokemon):
    attack  = 15 # base levels for grass pokemon
    defense = 14
    health  = 12
    p_type  = "Grass"

    attack_boost  = 2 # when we "train", how much to increment by
    defense_boost = 3
    health_boost  = 6

    evolution_threshold = 12 # How many times we need to train before we "evolve"
    def __init__(self,name):
        super().__init__(name)


    def moves(self):
        self.p_moves = ["razor leaf", "synthesis", "petal dance"]

    def action(self):
        return f"{self.name} knows a lot of different moves!"

p1 = Grass_Pokemon('Belle')
assert p1.action() == "Belle knows a lot of different moves!"

# 2

class Grass_Pokemon(Pokemon):
    attack  = 15 # base levels for grass pokemon
    defense = 14
    health  = 12
    p_type  = "Grass"

    attack_boost  = 2 # when we "train", how much to increment by
    defense_boost = 3
    health_boost  = 6

    evolution_threshold = 12 # How many times we need to train before we "evolve"
    def __init__(self,name, level = 5):
        super().__init__(name, level)


    def moves(self):
        self.p_moves = ["razor leaf", "synthesis", "petal dance"]

    def action(self):
        return f"{self.name} knows a lot of different moves!"

    def attack_str(self):
        if self.level >= 10:
            Grass_Pokemon.attack += Grass_Pokemon.attack_boost

p1 = Grass_Pokemon('Belle')
assert p1.action() == "Belle knows a lot of different moves!"

p2 = Grass_Pokemon('Bulby')
p3 = Grass_Pokemon('Pika')

for _ in range(10):
    p3.train()

assert isinstance(p2, Grass_Pokemon), "p2 is not the correct type"
assert isinstance(p3, Grass_Pokemon), "p3 is not the correct type"

assert p2.__str__() == "Pokemon name: Bulby, Type: Grass, Level: 5", "p2 does not have the correct value"
assert p3.level >= 10, "p3 does not have the correct level; only train to level 10"
assert p3.attack_up() >= 17, "p3 does not have the correct attack value at level 10"

# 3
import time
import functools

def performance(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = f(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        return result, elapsed_time
    return wrapper
