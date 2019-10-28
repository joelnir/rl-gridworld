import random
import numpy as np

def random_policy(grid_world):
    return random.randint(0, 3)

def greedy_policy(grid_world):
    pos = grid_world.get_position()

    # Sample uniformly from  argmax set
    Q_s = grid_world.q[pos[0], pos[1]]
    argmax = np.argwhere(Q_s == np.amax(Q_s))[:,0]
    argmax_size = argmax.shape[0]

    if argmax_size == 1:
        return argmax[0]
    else:
        return argmax[random.randint(0,argmax_size-1)]

def eps_greedy_policy(grid_world):
    if random.random() > grid_world.epsilon:
        return greedy_policy(grid_world)
    else:
        return random_policy(grid_world)
