from render import render
from space import space
from random import random
import numpy as np


amount = 70000
s = space(1920, 1080, amount, focii=(300, 300))
colors = [(255, 0, int(random()*255)) for i in range(amount)]
colors = list(np.array(colors).flatten())

r = render(s, colors)
