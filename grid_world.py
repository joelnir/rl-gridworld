import numpy as np

TILE_W = 6
TILE_H = 4

class GridWorld():
    def __init__(self):
        self.q = np.zeros((TILE_H, TILE_W))
        self.reward = np.zeros((TILE_H, TILE_W))

        self.policy = (lambda pos: (0,1))

        self.agent_pos = [0,0]

        # List of observers
        self.observers = []

    def step(self):
        # Take one step following current policy
        pos_delta = self.policy(self.agent_pos)
        self.agent_pos[0] = max(0, min(TILE_H-1, self.agent_pos[0] + pos_delta[0]))
        self.agent_pos[1] = max(0, min(TILE_W-1, self.agent_pos[1] + pos_delta[1]))
        print(self.agent_pos)

        # TODO Q-learning

        self.update()

    def set_policy(self, new_policy):
        self.policy = new_policy

    def update_q(self, new_q, x, y):
        self.q[y, x] = new_q
        self.update()

    def update_reward(self, new_reward, x, y):
        self.reward[y, x] = new_reward
        self.update()

    def get_q(self, x, y):
        return self.q[y, x]

    def get_reward(self, x, y):
        return self.reward[y, x]

    def get_size(self):
        return self.q.shape

    def get_position(self):
        return tuple(self.agent_pos)

    def add_observer(self, observer):
        self.observers.append(observer)

    # Tell all observers to repaint
    def update(self):
        for obs in self.observers:
            obs.repaint()
