# A random game with dictionaries

import random
trial_game = {
    1: "Hurt Locker",
    2: "Interstellar",
    3: "Dark Knight",
    4: "Django Unchained",
    5: "Madmax Fury Road"
}

print(trial_game)
var = random.randint(1, 11)
print("Movie of the day : - " + (trial_game.get(var, "Go and feed the cow!")))
